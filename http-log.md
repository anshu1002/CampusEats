# HTTP Request Log

# Request 1 — Get Post 1

# Command

curl -i https://jsonplaceholder.typicode.com/posts/1

# Full Response

C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/posts/1

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 13:30:39 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 292

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1785194657"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1785194657"

Server: cloudflare

vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1785194663
Age: 19556
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2b050bcec03ff6b-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,

  "id": 1,

  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",

  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

}

# Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing post information.

# Observation

The request was successful and the server returned a JSON response containing post data.


# Request 2 — Get Post 2

# Command

curl -i https://jsonplaceholder.typicode.com/posts/2

# Full Response

C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/posts/2

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 13:33:41 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 278

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"116-jnDuMpjju89+9j7e0BqkdFsVRjs"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}

pragma: no-cache

report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=AyDEJzv2CFP160WD%2F3JdlYGmQ%2BrTTe1sKm7ePc248Ko%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786352212"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=AyDEJzv2CFP160WD%2F3JdlYGmQ%2BrTTe1sKm7ePc248Ko%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786352212"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-limit: 1000

x-ratelimit-remaining: 952

x-ratelimit-reset: 1786352214

Age: 341

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2b055312c277d83-BOM

alt-svc: h3=":443"; ma=86400

{
  "userId": 1,

  "id": 2,

  "title": "qui est esse",

  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"

}

# Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8

- Response: JSON object containing post information.

# Observation

The request was successful and the server returned a JSON response containing post data.


# Request 3 — Get User 1

# Command

curl -i https://jsonplaceholder.typicode.com/users/1

# Full Response
C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/users/1

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 13:35:12 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 509

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"1fd-+2Y3G3w049iSZtw5t1mzSnunngE"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}

pragma: no-cache

report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?
s=vFqOaN78YYvn6a2s7ua%2FV7pltJEaqH%2Foz67ApraiMaU%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786552366"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vFqOaN78YYvn6a2s7ua%2FV7pltJEaqH%2Foz67ApraiMaU%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786552366"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1786552375

Age: 17576

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2b05769a84c49a6-BOM

alt-svc: h3=":443"; ma=86400

{
  "id": 1,

  "name": "Leanne Graham",

  "username": "Bret",

  "email": "Sincere@april.biz",

  "address": {    
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },

  "phone": "1-770-736-8031 x56442",

  "website": "hildegard.org",

  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}

# Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing user information.

# Observation

The request was successful and the server returned a JSON response containing user data.


# Request 4 — Get User 2

# Command

curl -i https://jsonplaceholder.typicode.com/users/2

# Full Response

C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/users/2

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 13:36:56 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 509

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"1fd-XTG63SYhaP/Uo6/vgmARnL3rpBk"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=QPAnKfzcZr%2B7jt4zABk8fHJbUmVPE%2Bq0YRdhLldcR%2Fw%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786328764"}],"max_age":3600}

reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=QPAnKfzcZr%2B7jt4zABk8fHJbUmVPE%2Bq0YRdhLldcR%2Fw%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786328764"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-limit: 1000

x-ratelimit-remaining: 948

x-ratelimit-reset: 1786328814

Age: 13566

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2b059f0a987ffc8-BOM

alt-svc: h3=":443"; ma=86400

{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}

# Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing user information.

# Observation

The request was successful and the server returned a JSON response containing user data.


# Request 5 — Get Comment 1

# Command

curl -i https://jsonplaceholder.typicode.com/comments/1

# Full Response

C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/comments/1

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 13:38:34 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 268

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"10c-KJ4I9RM/+33TKdV8CFsIvqsDSP0"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}

pragma: no-cache

report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=P0Lz72Y9QZasnK9TBAw%2Bz03v%2FNWX%2FOQUONOqSdgZxU8%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786686166"}],"max_age":3600}

reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=P0Lz72Y9QZasnK9TBAw%2Bz03v%2FNWX%2FOQUONOqSdgZxU8%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786686166"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1786686190

Age: 28548

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2b05c555b1d4199-BOM

alt-svc: h3=":443"; ma=86400

{
  "postId": 1,

  "id": 1,

  "name": "id labore ex et quam laborum",

  "email": "Eliseo@gardner.biz",

  "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

}

# Response

- Status: 200 OK
- Content-Type: application/json; charset=utf-8
- Response: JSON object containing comment information.

# Observation

The request was successful and the server returned a JSON response containing comment data.


# Request 6 — Deliberate Failure

# Command

curl -i https://jsonplaceholder.typicode.com/this-does-not-exist

# Full Response

C:\Users\Anshumala>curl -i https://jsonplaceholder.typicode.com/this-does-not-exist

HTTP/1.1 404 Not Found

Date: Fri, 14 Aug 2026 13:39:48 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 2

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"

expires: -1

nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}

pragma: no-cache

report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=FlAOERx7hWmOgXD%2BA8Nq%2BhJuzlyEwJCL9B9EMRCsbvc%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786714788"}],"max_age":3600}

reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=FlAOERx7hWmOgXD%2BA8Nq%2BhJuzlyEwJCL9B9EMRCsbvc%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786714788"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1786714810

cf-cache-status: MISS

CF-RAY: a2b05e215eac3fc6-BOM

alt-svc: h3=":443"; ma=86400

{}

# Response

- Status: 404 Not Found
- Content-Type: application/json; charset=utf-8

# Observation

The request was deliberately sent to a non-existent endpoint. The server returned 404 Not Found, indicating that the requested resource could not be found.


# Status Code Meaning

- 200 OK — The request was successfully processed.
- 404 Not Found — The requested resource could not be found.

# Content-Type Meaning

application/json indicates that the response body is in JSON format.