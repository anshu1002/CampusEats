const mysql = require("mysql2/promise");

// Update these values if your local MySQL username/password are different.
// The database is created by running schema.sql in MySQL Workbench.
const pool = mysql.createPool({
  host: process.env.DB_HOST || "localhost",
  user: process.env.DB_USER || "root",
  password: process.env.DB_PASSWORD || "Anshu210@",
  database: process.env.DB_NAME || "ORDERDATABASE",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

module.exports = pool;