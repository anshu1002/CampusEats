from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import uuid
import os
import urllib.request
import urllib.error
import time
import random

from urllib.parse import urlparse, parse_qs

from models import Order, OrderItem, validate
from store import OrderStore
from errors import problem


store = OrderStore()

# Stores previous successful responses for Idempotency-Key
idempotency_store = {}


# -------------------------
# PAYMENT SERVICE
# -------------------------

def call_payment_service(order_id):

    payment_url = os.environ.get("PAYMENT_SERVICE_URL")

    if not payment_url:
        raise RuntimeError(
            "PAYMENT_SERVICE_URL is not configured"
        )

    url = payment_url + "/payments/authorize"

    data = json.dumps({
        "order_id": order_id
    }).encode("utf-8")

    # Maximum 3 attempts
    max_attempts = 3

    for attempt in range(max_attempts):

        request = urllib.request.Request(
            url,
            data=data,
            method="POST",
            headers={
                "Content-Type": "application/json"
            }
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=3
            ) as response:

                return json.loads(
                    response.read().decode("utf-8")
                )

        except urllib.error.HTTPError as error:

            # 4xx errors must NOT be retried
            if 400 <= error.code < 500:
                raise

            # If this was the last attempt, stop
            if attempt == max_attempts - 1:
                raise

        except (
            urllib.error.URLError,
            TimeoutError
        ):

            # Network/timeout failure
            if attempt == max_attempts - 1:
                raise

        # Exponential backoff + jitter
        delay = (2 ** attempt) + random.uniform(0, 0.5)

        print(
            f"Payment request failed. "
            f"Retrying in {delay:.2f} seconds..."
        )

        time.sleep(delay)


# -------------------------
# ORDER HANDLER
# -------------------------

class OrderHandler(BaseHTTPRequestHandler):

    def send_json(
        self,
        status_code,
        data,
        content_type="application/json"
    ):

        body = json.dumps(data).encode("utf-8")

        self.send_response(status_code)

        self.send_header(
            "Content-Type",
            content_type
        )

        self.send_header(
            "Content-Length",
            str(len(body))
        )

        self.end_headers()

        self.wfile.write(body)


    def read_json_body(self):

        content_length = int(
            self.headers.get(
                "Content-Length",
                0
            )
        )

        body = self.rfile.read(content_length)

        try:
            return json.loads(body)

        except json.JSONDecodeError:
            return None


    # -------------------------
    # POST REQUESTS
    # -------------------------

    def do_POST(self):

        parsed_url = urlparse(self.path)

        path = parsed_url.path

        if path == "/orders":

            self.create_order()

            return

        if (
            path.startswith("/orders/")
            and path.endswith("/cancellation")
        ):

            order_id = path.split("/")[2]

            self.cancel_order(order_id)

            return

        self.send_json(
            404,
            problem(
                "not_found",
                "Not Found",
                404,
                "The requested resource does not exist."
            ),
            "application/problem+json"
        )


    # -------------------------
    # GET REQUESTS
    # -------------------------

    def do_GET(self):

        parsed_url = urlparse(self.path)

        path = parsed_url.path

        query = parse_qs(
            parsed_url.query
        )

        if path == "/orders":

            self.list_orders(query)

            return

        if path.startswith("/orders/"):

            order_id = path.split("/")[2]

            self.get_order(order_id)

            return

        self.send_json(
            404,
            problem(
                "not_found",
                "Not Found",
                404,
                "The requested resource does not exist."
            ),
            "application/problem+json"
        )


    # -------------------------
    # CREATE ORDER
    # -------------------------

    def create_order(self):

        # Get Idempotency-Key
        idempotency_key = self.headers.get(
            "Idempotency-Key"
        )

        # Check if request was already processed
        if (
            idempotency_key
            and idempotency_key in idempotency_store
        ):

            original_response = idempotency_store[
                idempotency_key
            ]

            self.send_response(
                original_response["status"]
            )

            self.send_header(
                "Location",
                original_response["location"]
            )

            self.send_header(
                "Content-Type",
                "application/json"
            )

            body = json.dumps(
                original_response["body"]
            ).encode("utf-8")

            self.send_header(
                "Content-Length",
                str(len(body))
            )

            self.end_headers()

            self.wfile.write(body)

            return


        # -------------------------
        # READ REQUEST BODY
        # -------------------------

        data = self.read_json_body()

        if data is None:

            self.send_json(
                400,
                problem(
                    "malformed_request",
                    "Malformed Request",
                    400,
                    "Request body must contain valid JSON."
                ),
                "application/problem+json"
            )

            return


        # -------------------------
        # VALIDATE REQUEST
        # -------------------------

        valid, error_message = validate(data)

        if not valid:

            self.send_json(
                400,
                problem(
                    "invalid_request",
                    "Invalid Request",
                    400,
                    error_message
                ),
                "application/problem+json"
            )

            return


        # -------------------------
        # CREATE ITEMS
        # -------------------------

        items = []

        for item in data["items"]:

            items.append(
                OrderItem(
                    item["item_id"],
                    item["quantity"]
                )
            )


        # -------------------------
        # GENERATE ORDER ID
        # -------------------------

        order_id = str(
            uuid.uuid4()
        )


        # -------------------------
        # CREATE ORDER
        # -------------------------

        order = Order(
            order_id,
            data["customer_id"],
            items
        )


        # -------------------------
        # CALL PAYMENT SERVICE
        # -------------------------

        try:

            payment_response = call_payment_service(
                order_id
            )

        except Exception:

            self.send_json(
                503,
                problem(
                    "payment_service_unavailable",
                    "Payment Service Unavailable",
                    503,
                    "The payment service could not be reached."
                ),
                "application/problem+json"
            )

            return


        # -------------------------
        # STORE ORDER
        # -------------------------

        store.create(order)


        # -------------------------
        # PREPARE RESPONSE
        # -------------------------

        response_body = order.as_json()

        location = "/orders/" + order_id


        # -------------------------
        # SAVE IDEMPOTENCY RESULT
        # -------------------------

        if idempotency_key:

            idempotency_store[
                idempotency_key
            ] = {
                "status": 201,
                "location": location,
                "body": response_body
            }


        # -------------------------
        # SEND RESPONSE
        # -------------------------

        self.send_response(201)

        self.send_header(
            "Location",
            location
        )

        self.send_header(
            "Content-Type",
            "application/json"
        )

        body = json.dumps(
            response_body
        ).encode("utf-8")

        self.send_header(
            "Content-Length",
            str(len(body))
        )

        self.end_headers()

        self.wfile.write(body)


    # -------------------------
    # GET ONE ORDER
    # -------------------------

    def get_order(self, order_id):

        order = store.get(order_id)

        if order is None:

            self.send_json(
                404,
                problem(
                    "order_not_found",
                    "Order Not Found",
                    404,
                    "The requested order does not exist."
                ),
                "application/problem+json"
            )

            return

        self.send_json(
            200,
            order.as_json()
        )


    # -------------------------
    # LIST ORDERS
    # -------------------------

    def list_orders(self, query):

        customer_id = query.get(
            "customer_id",
            [None]
        )[0]

        status = query.get(
            "status",
            [None]
        )[0]

        orders = store.list(
            customer_id=customer_id,
            status=status
        )

        result = [
            order.as_json()
            for order in orders
        ]

        self.send_json(
            200,
            result
        )


    # -------------------------
    # CANCEL ORDER
    # -------------------------

    def cancel_order(self, order_id):

        order = store.get(order_id)

        # Order doesn't exist
        if order is None:

            self.send_json(
                404,
                problem(
                    "order_not_found",
                    "Order Not Found",
                    404,
                    "The requested order does not exist."
                ),
                "application/problem+json"
            )

            return


        # Already cancelled
        if order.status == "cancelled":

            self.send_json(
                409,
                problem(
                    "invalid_state",
                    "Order Cannot Be Cancelled",
                    409,
                    "The order is already cancelled."
                ),
                "application/problem+json"
            )

            return


        # Cancel order
        order.status = "cancelled"

        store.update(order)

        self.send_json(
            200,
            order.as_json()
        )


# -------------------------
# START SERVER
# -------------------------

if __name__ == "__main__":

    server = HTTPServer(
        ("127.0.0.1", 5000),
        OrderHandler
    )

    print(
        "CampusEats Orders API running on "
        "http://127.0.0.1:5000"
    )

    server.serve_forever()