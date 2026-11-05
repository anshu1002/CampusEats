# CampusEats REST API

## Project Description

CampusEats REST API is a simple Node.js and Express.js application that manages food items. It provides REST endpoints to retrieve all items, retrieve a single item by ID, and add new items.

The application uses an in-memory array to store food records and a simple HTML, CSS, and JavaScript frontend to interact with the API.

## Technologies Used

- Node.js
- Express.js
- HTML
- CSS
- JavaScript
- REST API

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/items` | Retrieve all food items |
| GET | `/items/:id` | Retrieve an item by ID |
| POST | `/items` | Add a new food item |

## HTTP Status Codes

- **200 OK:** Request successful.
- **201 Created:** New item successfully created.
- **404 Not Found:** Requested item does not exist.
- **422 Unprocessable Entity:** Required fields are missing or invalid.

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/anshu1002/CampusEats.git
   ```
   Demonstration Video:- https://drive.google.com/file/d/1jPbuTqeB8FfikdbowGII3nfCW2jPxNW2/view?usp=sharing

2. Navigate to the REST service folder:

   ```bash
   cd CampusEats/rest_service
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Start the server:

   ```bash
   node server.js
   ```

5. Open the browser:

   ```text
   http://localhost:4000
   ```

## Screenshots

- `before.png` – Initial food item listing.
- `after.png` – Food item listing after adding a new item.

## Team Members

| Name | Roll Number |
|---|---|
| Anshu Mala | 20252651010 |
| Mritunjay Maurya | 20252651035 |
| Sanika Jain | 20252651046 |
| Annu Mishra | 20252651009 |

## Learning Outcomes

- Understanding REST API architecture.
- Implementing GET and POST routes using Express.js.
- Handling request parameters and JSON request bodies.
- Implementing input validation and HTTP status codes.
- Connecting a frontend with backend APIs using Fetch API.

## Assignment Questions and Answers

### 1. Which CampusEats service did you pick, and what are its routes (method + path)?

We selected the **Menu/Catalogue service** of CampusEats. It manages food items and provides the following REST API routes:

- GET `/items` – Retrieves all food items.
- GET `/items/:id` – Retrieves a specific food item using its ID.
- POST `/items` – Creates a new food item.

### 2. Which status codes did you return, and for which outcomes (200 / 201 / 404 / 422)?

We used the following HTTP status codes:

- **200 OK:** Returned when food items are successfully retrieved.
- **201 Created:** Returned when a new food item is successfully created.
- **404 Not Found:** Returned when the requested food item ID does not exist.
- **422 Unprocessable Entity:** Returned when required fields such as name or price are missing or invalid in the POST request.

### 3. Where did you use req.params and where req.body? Why does POST need express.json()?

- **req.params:** Used in GET `/items/:id` to retrieve the item ID from the URL.
- **req.body:** Used in POST `/items` to access the data sent by the client, such as the item's name and price.
- **express.json():** It is middleware that parses incoming JSON request bodies and makes the parsed data available through `req.body`. Without it, Express cannot automatically read JSON request data through `req.body`.

## GitHub Repository

https://github.com/anshu1002/CampusEats