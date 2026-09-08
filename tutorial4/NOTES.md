# CampusEats — Assignment 4: Rebuilding Orders in REST

## Team Members

| S.No. | Name             |     Roll No:-     |
|   1   | Anshu Mala       | 20252651010 |
|   2   | Annu Mishra      | 20252651009 |
|   3   | Sanika Jain      | 20252651046 |
|   4   | Mritunjay Maurya | 20252651035 |

---

# Part A — REST Resource Design

## A1. Service

**Orders Service**

The Orders Service is responsible for creating, retrieving, listing, and cancelling customer orders.

---

## A2. Original SOAP Operations

| Operation                        | Description                    |
| -------------------------------- | ------------------------------ |
| `createOrder(customerId, items)` | Creates a new customer order   |
| `getOrder(orderId)`              | Retrieves an existing order    |
| `listOrders(customerId, status)` | Retrieves orders using filters |
| `cancelOrder(orderId)`           | Cancels an existing order      |

---

## A3. REST Resource Table

| Resource / Endpoint                       | HTTP Method | Purpose                   | Success Response                  | Error Responses                                                            |
| ----------------------------------------- | :---------: | ------------------------- | --------------------------------- | -------------------------------------------------------------------------- |
| `/orders`                                 |    `POST`   | Create a new order        | `201 Created` + `Location` header | `400 Bad Request`, `422 Payment Failed`, `503 Payment Service Unavailable` |
| `/orders/{orderId}`                       |    `GET`    | Retrieve a specific order | `200 OK`                          | `404 Not Found`                                                            |
| `/orders?customer_id=C001&status=created` |    `GET`    | List/filter orders        | `200 OK`                          | `400 Bad Request`                                                          |
| `/orders/{orderId}/cancellation`          |    `POST`   | Cancel an order           | `200 OK`                          | `404 Not Found`, `409 Conflict`                                            |

---

## A4. REST Resource Design

| Resource          | URI                              | Method | Description                          |
| ----------------- | -------------------------------- | :----: | ------------------------------------ |
| Orders Collection | `/orders`                        | `POST` | Creates a new order                  |
| Orders Collection | `/orders`                        |  `GET` | Lists orders using query filters     |
| Single Order      | `/orders/{orderId}`              |  `GET` | Retrieves one order                  |
| Cancellation      | `/orders/{orderId}/cancellation` | `POST` | Changes the order state to cancelled |

### REST Design Rules

| Rule                               | Implementation                      |
| ---------------------------------- | ----------------------------------- |
| Use nouns instead of verbs         | `/orders` instead of `/createOrder` |
| Use plural collection names        | `/orders`                           |
| Use path parameters for resources  | `/orders/{orderId}`                 |
| Use query parameters for filtering | `?customer_id=C001&status=created`  |
| Use sub-resource for cancellation  | `/orders/{orderId}/cancellation`    |

---

## A5. Resource Representation

The public order representation contains only information required by API clients.

| Field         | Type   | Description                 |
| ------------- | ------ | --------------------------- |
| `order_id`    | String | Unique order identifier     |
| `customer_id` | String | Customer identifier         |
| `items`       | Array  | Items included in the order |
| `status`      | String | Current order status        |
| `payment_id`  | String | Payment identifier          |
| `amount`      | Number | Total order amount          |

Internal database identifiers such as `internal_id` are not exposed to clients.

### Example

```json
{
  "order_id": "O-123ABC",
  "customer_id": "C001",
  "items": [
    {
      "item_id": "I001",
      "quantity": 2,
      "unit_price": 100
    }
  ],
  "status": "created",
  "payment_id": "PAY-123ABC",
  "amount": 200
}
```

---

# Part B — HTTP Request and Response Examples

## B1. Create Order

### Request

```http
POST /orders
Content-Type: application/json
Idempotency-Key: order-C001-001
```

```json
{
  "customer_id": "C001",
  "items": [
    {
      "item_id": "I001",
      "quantity": 2,
      "unit_price": 100
    }
  ]
}
```

### Successful Response

```http
HTTP/1.1 201 Created
Location: /orders/O-123ABC
Content-Type: application/json
```

```json
{
  "order_id": "O-123ABC",
  "customer_id": "C001",
  "items": [
    {
      "item_id": "I001",
      "quantity": 2,
      "unit_price": 100
    }
  ],
  "status": "created",
  "payment_id": "PAY-123ABC",
  "amount": 200
}
```

---

## B2. Get Order

### Request

```http
GET /orders/O-123ABC
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "order_id": "O-123ABC",
  "customer_id": "C001",
  "items": [
    {
      "item_id": "I001",
      "quantity": 2,
      "unit_price": 100
    }
  ],
  "status": "created"
}
```

---

## B3. List Orders

### Request

```http
GET /orders?customer_id=C001&status=created
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
[
  {
    "order_id": "O-123ABC",
    "customer_id": "C001",
    "items": [
      {
        "item_id": "I001",
        "quantity": 2,
        "unit_price": 100
      }
    ],
    "status": "created"
  }
]
```

---

## B4. Cancel Order

### Request

```http
POST /orders/O-123ABC/cancellation
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "order_id": "O-123ABC",
  "customer_id": "C001",
  "items": [
    {
      "item_id": "I001",
      "quantity": 2,
      "unit_price": 100
    }
  ],
  "status": "cancelled"
}
```

---

# Part C — OpenAPI Contract

The Orders Service is documented using **OpenAPI**.

The `openapi.yaml` contract defines:

| OpenAPI Component    | Purpose                            |
| -------------------- | ---------------------------------- |
| `paths`              | REST endpoints and HTTP methods    |
| `parameters`         | Path, query, and header parameters |
| `requestBody`        | JSON request structure             |
| `responses`          | HTTP responses and status codes    |
| `components.schemas` | Data models                        |
| `servers`            | Base API URL                       |

The API includes:

* `POST /orders`
* `GET /orders`
* `GET /orders/{orderId}`
* `POST /orders/{orderId}/cancellation`
* `GET /health`

---

# Part D — Cross-Service Communication

## D1. Payment Service Communication

The Orders Service communicates with the Payment Service when creating an order.

### Flow

```text
Client
   |
   | POST /orders
   v
Orders Service
   |
   | POST /payments/authorize
   | Idempotency-Key
   v
Payment Service
```

The Payment Service URL is configured using:

```text
PAYMENT_SERVICE_URL
```

Example:

```text
PAYMENT_SERVICE_URL=http://payment-service:8081
```

The Orders Service stores the order **only after payment authorization succeeds**.

---

## D2. Retry Strategy

The Orders Service uses a hardened HTTP client for communication with the Payment Service.

| Configuration             | Value                    |
| ------------------------- | ------------------------ |
| Maximum attempts          | 3                        |
| Request timeout           | 3 seconds                |
| Network/connection errors | Retry                    |
| Timeout errors            | Retry                    |
| Server-side `5xx` errors  | Retry                    |
| Client-side `4xx` errors  | Do not retry             |
| Backoff                   | Exponential              |
| Jitter                    | Random delay             |
| Idempotency key           | Same key for every retry |

### Backoff Formula

```text
delay = 2^attempt + random jitter
```

The same idempotency key is reused for every retry so that the Payment Service does not create duplicate payment transactions.

---

## D3. Idempotency

The client sends an `Idempotency-Key` with the order creation request.

Example:

```http
Idempotency-Key: order-C001-001
```

If the client retries the same request using the same key:

| Situation                   | Result                               |
| --------------------------- | ------------------------------------ |
| First request succeeds      | Order is created                     |
| Same key is received again  | Existing order is returned           |
| Payment request is retried  | Same payment idempotency key is used |
| Payment remains unavailable | `503 Service Unavailable`            |
| Order after failed payment  | Not stored                           |

This prevents duplicate orders and duplicate payment attempts.

---

# Part E — Error Handling and Fallback

## E1. Error Response Table

| Situation                   | HTTP Status | Meaning                              |
| --------------------------- | :---------: | ------------------------------------ |
| Invalid request             |    `400`    | Client sent invalid data             |
| Order not found             |    `404`    | Requested order does not exist       |
| Payment failed              |    `422`    | Payment authorization was rejected   |
| Invalid cancellation state  |    `409`    | Order cannot be cancelled            |
| Payment Service unavailable |    `503`    | Payment service could not be reached |

---

## E2. Payment Service Unavailable

If the Payment Service is unavailable:

1. Orders Service attempts the request up to 3 times.
2. Each attempt has a 3-second timeout.
3. Exponential backoff with jitter is used.
4. If all attempts fail, the Orders Service returns `503`.
5. The order is **not stored**.
6. The client can retry later using the same idempotency key.

### Example

```json
{
  "type": "about:blank",
  "title": "Payment Service Unavailable",
  "status": 503,
  "detail": "Payment service could not be reached after the configured retries."
}
```

---

# Part F — SOAP to REST Questions

## Q1. WSDL vs OpenAPI

| Feature         | WSDL / SOAP     | OpenAPI / REST                       |
| --------------- | --------------- | ------------------------------------ |
| Contract format | XML             | YAML/JSON                            |
| Operations      | SOAP operations | HTTP methods                         |
| Messages        | `wsdl:message`  | Request/response bodies              |
| Data types      | `wsdl:types`    | `components.schemas`                 |
| Binding         | SOAP binding    | HTTP                                 |
| Endpoint        | Service/Port    | `servers.url`                        |
| Errors          | SOAP Fault      | HTTP status codes + problem response |

### Mapping

| WSDL Element                 | OpenAPI Equivalent                       |
| ---------------------------- | ---------------------------------------- |
| `wsdl:types`                 | `components.schemas`                     |
| `wsdl:message`               | `requestBody` / `responses`              |
| `wsdl:portType`              | `paths` + HTTP methods                   |
| `wsdl:binding`               | HTTP semantics; no separate SOAP binding |
| `wsdl:service` / `wsdl:port` | `servers.url`                            |
| `soap:Fault`                 | HTTP error response                      |

The exact number of lines in `partner.wsdl` cannot be determined from the provided Assignment 3 write-up because the raw WSDL file itself was not provided.

---

## Q2. SOAP Fault Mapping

Assignment 3 describes the following PayFlex SOAP faults:

| PayFlex SOAP Fault   | CampusEats Handling                     |
| -------------------- | --------------------------------------- |
| `card_declined`      | `PaymentFailed`                         |
| `gateway_timeout`    | `PaymentFailed` / availability handling |
| `invalid_card_token` | `PaymentFailed`                         |
| `insufficient_funds` | `PaymentFailed`                         |

For the REST Orders Service, the main responses are:

| Condition                   | REST Response              |
| --------------------------- | -------------------------- |
| Invalid order data          | `400 Bad Request`          |
| Payment rejected            | `422 Unprocessable Entity` |
| Payment service unavailable | `503 Service Unavailable`  |

---

## Q3. Publish, Find and Bind in REST

In the SOAP/UDDI model, services can be published, discovered, and bound through a service registry.

In REST, this can be represented as:

| Step    | REST Approach                                             |
| ------- | --------------------------------------------------------- |
| Publish | Register service name, API URL, and OpenAPI documentation |
| Find    | Resolve the service name to its HTTP base URL             |
| Bind    | Send an HTTP request to the resolved URL                  |

Example:

```text
PAYMENT_SERVICE_URL=http://payment-service:8081
```

Unlike SOAP, REST does not require generating or binding a SOAP proxy. The client communicates directly using HTTP.

---

## Q4. Request Validation

The Orders Service validates the incoming JSON request before creating an order.

| Field / Check | Validation                 |
| ------------- | -------------------------- |
| Request body  | Must be a JSON object      |
| `customer_id` | Required non-empty string  |
| `items`       | Required non-empty array   |
| Each item     | Must be an object          |
| `item_id`     | Required non-empty string  |
| `quantity`    | Integer and `>= 1`         |
| `unit_price`  | Optional number and `>= 0` |

If validation fails:

```http
400 Bad Request
```

Example:

```json
{
  "type": "about:blank",
  "title": "Invalid order",
  "status": 400,
  "detail": "items must be a non-empty array."
}
```

---

## Q5. When SOAP May Still Be Preferred

SOAP may still be preferred when an organization requires:

* Strong formal contracts through WSDL
* WS-Security
* Enterprise security standards
* Reliable messaging
* Existing enterprise SOAP infrastructure
* Legacy partner integration

For example, a payment partner such as PayFlex may continue using SOAP because of its existing enterprise integration requirements.

REST is preferred for the CampusEats public API because it is simpler, resource-oriented, and uses standard HTTP semantics.

---

# Part G — Testing

The REST implementation should be tested for the following cases:

| Test Case                      | Expected Result    |
| ------------------------------ | ------------------ |
| Valid order creation           | `201 Created`      |
| Invalid order data             | `400 Bad Request`  |
| Missing idempotency key        | `400 Bad Request`  |
| Get existing order             | `200 OK`           |
| Get unknown order              | `404 Not Found`    |
| Filter orders                  | `200 OK`           |
| Invalid filter request         | `400 Bad Request`  |
| Cancel existing order          | `200 OK`           |
| Cancel unknown order           | `404 Not Found`    |
| Cancel already cancelled order | `409 Conflict`     |
| Payment rejected               | `422`              |
| Payment service unavailable    | `503`              |
| Repeat same idempotency key    | No duplicate order |

---

# Part H — Final Summary

The Orders Service has been redesigned from a SOAP-style service into a REST-based service following the principles of Tutorial 4.

The implementation demonstrates:

* Resource-oriented REST URLs
* HTTP methods
* HTTP status codes
* OpenAPI contract
* JSON representations
* Request validation
* Payment Service integration
* Timeout handling
* Retry with exponential backoff and jitter
* Idempotency
* Error handling
* Service discovery using a resolvable URL
* Docker-based service separation
* Automated testing

The design replaces SOAP/WSDL-specific interaction with REST resources, HTTP semantics, OpenAPI documentation, and service URLs while keeping the required payment-service reliability and error-handling behavior.
