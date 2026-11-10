# CampusEats REST API

## Project Description

CampusEats REST API is a Node.js and Express.js application that manages food items for a campus canteen.

It provides REST endpoints to retrieve all food items, retrieve a single item by ID, and add new food items.

The application uses an in-memory array to store food records and a simple HTML, CSS, and JavaScript frontend to interact with the API.

In this assignment, security features have also been implemented using JWT Authentication and Role-Based Authorization to protect API endpoints.

## Technologies Used

- Node.js
- Express.js
- HTML
- CSS
- JavaScript
- REST API
- JSON Web Token (JWT)
- bcryptjs
- dotenv
- Postman

## API Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| POST | `/login` | Login and generate JWT token | Public |
| GET | `/items` | Retrieve all food items | Authenticated users |
| GET | `/items/:id` | Retrieve an item by ID | Authenticated users |
| POST | `/items` | Add a new food item | Restaurant role only |

## HTTP Status Codes

- **200 OK:** Request successful or login successful.
- **201 Created:** New food item successfully created.
- **401 Unauthorized:** Authentication token is missing, invalid, or expired, or login credentials are incorrect.
- **403 Forbidden:** Authenticated user does not have the required role.
- **404 Not Found:** Requested item does not exist.
- **422 Unprocessable Entity:** Required fields are missing or invalid.

## Authentication and Authorization

### 1. Password Security

Two users with different roles are seeded in the application:

| Email | Password | Role |
|---|---|---|
| customer@ampuseats.com | customer123 | customer |
| restaurant@campus.com | restaurant123 | restaurant |

Passwords are stored as bcrypt hashes instead of plain-text passwords.

### 2. JWT Authentication

The `/login` endpoint verifies user credentials using `bcrypt.compareSync()`.

After successful login, the server generates a JWT token using `jwt.sign()`.

The token contains:

- `sub`: User ID
- `role`: User role

The token expires after one hour.

### 3. Authentication Middleware

The `auth` middleware:

- Reads the token from the Authorization header.
- Checks the Bearer token.
- Verifies the token using `jwt.verify()`.
- Returns 401 Unauthorized if the token is missing, invalid, or expired.

### 4. Role-Based Authorization

The `requireRole()` middleware checks whether the authenticated user has permission to perform an operation.

- Customers can retrieve food items.
- Restaurant users can retrieve food items and create new food items.
- Customers cannot create new food items.

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/anshu1002/CampusEats.git
   ```

2. Navigate to the REST service folder:

   ```bash
   cd CampusEats/rest_service
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Create a `.env` file in the `rest_service` folder and add your JWT secret:

   ```env
   JWT_SECRET=your_long_random_secret_key
   ```

   You can refer to `.env.example` for the required environment variable.

5. Start the server:

   ```bash
   node server.js
   ```

6. Open the application in your browser:

   ```text
   http://localhost:4000
   ```

## Security Test Cases

### Case 1: Request without authentication token

Request:

```http
GET /items
```

Expected response:

**401 Unauthorized**

```json
{
  "error": "Access token is required"
}
```

Explanation: The request is rejected because the user has not provided an authentication token.

### Case 2: Successful login

Request:

```http
POST /login
```

Expected response:

**200 OK**

```json
{
  "message": "Login successful",
  "token": "<JWT_TOKEN>"
}
```

Explanation: The server verifies the user's credentials and generates a JWT token.

### Case 3: Customer tries to create a food item

Request:

```http
POST /items
```

Expected response:

**403 Forbidden**

```json
{
  "error": "You do not have permission to perform this action"
}
```

Explanation: The customer is authenticated but does not have the restaurant role.

### Case 4: Restaurant creates a food item

Request:

```http
POST /items
```

Example request body:

```json
{
  "name": "Pasta",
  "price": 120
}
```

Expected response:

**201 Created**

```json
{
  "id": 5,
  "name": "Pasta",
  "price": 120,
  "available": true
}
```

Explanation: The restaurant user is authenticated and authorized to create a new food item.

## Screenshots

- `before.png` – Initial food item listing.
- `after.png` – Food item listing after adding a new item.

## Demonstration Video

[CampusEats REST API Demonstration](https://drive.google.com/file/d/1jPbuTqeB8FfikdbowGII3nfCW2jPxNW2/view?usp=sharing)

## Team Members

| Name | Roll Number |
|---|---|
| Mritunjay Maurya | 20252651035 |
| Anshu Mala (Team Leader) | 20252651010 |
| Sanika Jain | 20252651046 |
| Annu Mishra | 20252651009 |

## Learning Outcomes

- Understanding REST API architecture.
- Implementing GET and POST routes using Express.js.
- Handling request parameters and JSON request bodies.
- Implementing input validation and HTTP status codes.
- Connecting a frontend with backend APIs using Fetch API.
- Understanding password hashing using bcrypt.
- Implementing JWT-based authentication.
- Protecting API endpoints using authentication middleware.
- Implementing role-based authorization.
- Understanding the difference between 401 Unauthorized and 403 Forbidden responses.
- Managing environment variables securely using dotenv.

## Assignment Questions and Answers

### Assignment 8: REST API

**1. Which CampusEats service did you pick, and what are its routes (method + path)?**

We selected the **Menu/Catalogue service** of CampusEats. It manages food items and provides the following REST API routes:

- GET `/items` – Retrieves all food items.
- GET `/items/:id` – Retrieves a specific food item using its ID.
- POST `/items` – Creates a new food item.

**2. Which status codes did you return, and for which outcomes (200 / 201 / 404 / 422)?**

- 200 OK: Returned when food items are successfully retrieved.
- 201 Created: Returned when a new food item is successfully created.
- 404 Not Found: Returned when the requested food item ID does not exist.
- 422 Unprocessable Entity: Returned when required fields such as name or price are missing or invalid.

**3. Where did you use req.params and where req.body? Why does POST need express.json()?**

- `req.params`: Used in GET `/items/:id` to retrieve the item ID from the URL.
- `req.body`: Used in POST `/items` to access data sent by the client, such as the item's name and price.
- `express.json()`: Middleware that parses incoming JSON request bodies and makes the parsed data available through `req.body`.

### Security Assignment

**1. Which routes require only authentication and which routes also require a specific role?**

Routes requiring authentication:

- GET `/items`
- GET `/items/:id`

Any authenticated user can access these routes.

Route requiring authentication and role-based authorization:

- POST `/items`

Only users with the restaurant role can create food items.

**2. Show one 401 response and one 403 response. What do they mean?**

- **401 Unauthorized:** Returned when the user does not provide a valid authentication token.
- **403 Forbidden:** Returned when the user is authenticated but does not have the required role to perform the operation.

**3. What information is stored in the JWT payload? Why can the server trust the role claim?**

The JWT payload contains the user's subject ID (`sub`) and role.

Example:

```json
{
  "sub": 2,
  "role": "restaurant"
}
```

The server trusts the role claim only after successfully verifying the JWT signature using the secret key. If the token is modified, signature verification fails.

**4. Why should the JWT secret be stored outside the source code?**

The JWT secret is sensitive information. Storing it directly in source code can expose it when the project is shared or uploaded to GitHub.

Therefore, the secret is stored in a `.env` file and accessed using `process.env.JWT_SECRET`. The `.env` file is excluded from Git using `.gitignore`, while `.env.example` is shared without the actual secret.

## GitHub Repository

[CampusEats GitHub Repository](https://github.com/anshu1002/CampusEats)