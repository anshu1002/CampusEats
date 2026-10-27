# CampusEats GraphQL Service — CS543 Assignment 7

## Team Members

1. Anshu Mala (20252651010)
2. Mritunjay Maurya (20252651035)
3. Sanika Jain (20252651046)
4. Annu Mishra (20252651009)

## Question 1: Which CampusEats service did you pick?

We picked the **Menu/Dishes service** of CampusEats. It allows clients to retrieve all dishes, retrieve a dish by its ID, and add a new dish using GraphQL.

## Question 2: Name one field a client can skip and one it cannot. What does GraphQL `!` mean?

A client can skip the `available` field in a GraphQL query because GraphQL allows clients to request only the fields they need.

A client cannot omit `name` from `AddDishInput` when providing input for the `addDish` mutation because `name: String!` is a required, non-null input field.

The `!` symbol means that a field cannot be `null`. For a required input field, the client must provide a value.

## Question 3: Map the GraphQL operations to SQL. Which query part became `WHERE`, and which resolver ran `INSERT`?

- **List dishes:** The `dishes` resolver executes `SELECT id, name, price, available FROM dishes ORDER BY id` to retrieve all dishes.
- **Retrieve one dish:** The `dish(id: ID!)` resolver executes `SELECT id, name, price, available FROM dishes WHERE id = ?`. The `id` argument is passed as a SQL parameter.
- **Add a dish:** The `addDish` resolver executes `INSERT INTO dishes (name, price, available) VALUES (?, ?, TRUE)` to insert a new dish. It then retrieves the inserted row using its generated ID.

## Requirements

- Node.js and npm
- MySQL Server and MySQL Workbench

## Run Instructions

1. Open MySQL Workbench and execute `schema.sql`. Run the seed section only once to avoid duplicate sample rows.
2. Check the MySQL credentials configured in `db.js`. If necessary, set the environment variables `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME`.
3. Open PowerShell in the `graphql_service` directory and run:

   ```powershell
   npm install
   npm start
   ```

4. Open the HTML/CSS page: http://localhost:4000
5. GraphQL endpoint: http://localhost:4000/graphql

## Demonstration and Screenshots

- **GitHub Repository:** [Paste your repository link here]
- **Demonstration Video (Google Drive):** [https://drive.google.com/file/d/1Rj8eL3V3bY6fZb8xzPCqDuMoWn8Recv3/view?usp=sharing]
- **Before Mutation Screenshot:** [https://drive.google.com/file/d/1E9jChlnuLuxLDigUvMrY1vyRIhTvJROo/view?usp=sharing]
- **After Mutation Screenshot:** [https://drive.google.com/file/d/1WDWRMhPTEXKUzqo1FPPb4xbUnERta6k6/view?usp=sharing]

Ensure the demonstration video and screenshots are accessible to the instructor.

