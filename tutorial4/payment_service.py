from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class PaymentHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/payments/authorize":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return

        response = {
            "payment_status": "approved",
            "order_id": data.get("order_id")
        }

        response_body = json.dumps(response).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()

        self.wfile.write(response_body)


server = HTTPServer(
    ("127.0.0.1", 5001),
    PaymentHandler
)

print("Payment Service running on http://localhost:5001")

server.serve_forever()