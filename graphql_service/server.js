const fs = require("fs");
const path = require("path");
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { ApolloServer } = require("@apollo/server");
const { expressMiddleware } = require("@apollo/server/express4");
const { gql } = require("graphql-tag");
const db = require("./db");

// Read the schema from the required schema.graphql file.
const typeDefs = gql(fs.readFileSync(path.join(__dirname, "schema.graphql"), "utf8"));

const resolvers = {
  Query: {
    // SQL SELECT: list all dishes.
    dishes: async () => {
      const [rows] = await db.execute(
        "SELECT id, name, price, available FROM dishes ORDER BY id"
      );
      return rows.map(row => ({
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      }));
    },

    // SQL SELECT with WHERE: fetch one dish by id.
    dish: async (_, { id }) => {
      const [rows] = await db.execute(
        "SELECT id, name, price, available FROM dishes WHERE id = ?",
        [Number(id)]
      );
      if (rows.length === 0) return null;
      const row = rows[0];
      return {
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      };
    }
  },

  Mutation: {
    // SQL INSERT: add one dish.
    addDish: async (_, { input }) => {
      const [result] = await db.execute(
        "INSERT INTO dishes (name, price, available) VALUES (?, ?, TRUE)",
        [input.name, input.price]
      );

      const [rows] = await db.execute(
        "SELECT id, name, price, available FROM dishes WHERE id = ?",
        [result.insertId]
      );
      const row = rows[0];
      return {
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      };
    }
  }
};

async function start() {
  const app = express();
  app.use(cors());
  app.use(express.static(path.join(__dirname, "public")));

  const apollo = new ApolloServer({ typeDefs, resolvers });
  await apollo.start();

  app.use(
    "/graphql",
    bodyParser.json(),
    expressMiddleware(apollo)
  );

  const port = process.env.PORT || 4000;
  app.listen(port, () => {
    console.log(`CampusEats page: http://localhost:${port}`);
    console.log(`GraphQL endpoint: http://localhost:${port}/graphql`);
  });
}

start().catch(error => {
  console.error("Could not start GraphQL service:", error.message);
  process.exit(1);
});