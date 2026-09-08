import json
import subprocess
import sys
import time
import urllib.request
import urllib.error


BASE_URL = "http://localhost:5000"


def request(method, path, body=None, headers=None):

    url = BASE_URL + path

    data = None

    if body is not None:
        data = json.dumps(body).encode("utf-8")

    request_obj = urllib.request.Request(
        url,
        data=data,
        method=method
    )

    if headers:
        for key, value in headers.items():
            request_obj.add_header(key, value)

    try:
        with urllib.request.urlopen(request_obj) as response:
            return (
                response.status,
                dict(response.headers),
                json.loads(response.read().decode("utf-8"))
            )

    except urllib.error.HTTPError as error:
        return (
            error.code,
            dict(error.headers),
            json.loads(error.read().decode("utf-8"))
        )


def test_create_order():

    status, headers, body = request(
        "POST",
        "/orders",
        {
            "customer_id": "TEST001",
            "items": [
                {
                    "item_id": "I001",
                    "quantity": 1
                }
            ]
        }
    )

    assert status == 201
    assert "Location" in headers
    assert body["customer_id"] == "TEST001"


def test_idempotent_repeat():

    order_data = {
        "customer_id": "TEST002",
        "items": [
            {
                "item_id": "I002",
                "quantity": 2
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Idempotency-Key": "pytest-key-001"
    }

    status1, headers1, body1 = request(
        "POST",
        "/orders",
        order_data,
        headers
    )

    status2, headers2, body2 = request(
        "POST",
        "/orders",
        order_data,
        headers
    )

    assert status1 == 201
    assert status2 == 201
    assert body1["order_id"] == body2["order_id"]
    assert headers1["Location"] == headers2["Location"]


def test_malformed_request():

    status, headers, body = request(
        "POST",
        "/orders",
        None,
        {
            "Content-Type": "application/json"
        }
    )

    assert status == 400


def test_unknown_order():

    status, headers, body = request(
        "GET",
        "/orders/does-not-exist"
    )

    assert status == 404