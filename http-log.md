# HTTP Request Log

## Request 1 — Get Post 1

### Command

curl -i https://jsonplaceholder.typicode.com/posts/1

### Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing post information.

### Observation

The request was successful and the server returned a JSON response containing post data.


## Request 2 — Get Post 2

### Command

curl -i https://jsonplaceholder.typicode.com/posts/2

### Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing post information.

### Observation

The request was successful and the server returned a JSON response containing post data.


## Request 3 — Get User 1

### Command

curl -i https://jsonplaceholder.typicode.com/users/1

### Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing user information.

### Observation

The request was successful and the server returned a JSON response containing user data.


## Request 4 — Get User 2

### Command

curl -i https://jsonplaceholder.typicode.com/users/2

### Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing user information.

### Observation

The request was successful and the server returned a JSON response containing user data.


## Request 5 — Get Comment 1

### Command

curl -i https://jsonplaceholder.typicode.com/comments/1

### Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing comment information.

### Observation

The request was successful and the server returned a JSON response containing comment data.


## Request 6 — Deliberate Failure

### Command

curl -i https://jsonplaceholder.typicode.com/this-does-not-exist

### Response

- Status: 404 Not Found
- Content-Type: application/json; charset=utf-8

### Observation

The request was deliberately sent to a non-existent endpoint. The server returned 404 Not Found, indicating that the requested resource could not be found.


## Status Code Meaning

- 200 OK — The request was successfully processed.
- 404 Not Found — The requested resource could not be found.

## Content-Type Meaning

application/json indicates that the response body is in JSON format.