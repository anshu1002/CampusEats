CREATE DATABASE IF NOT EXISTS ORDERDATABASE;
USE ORDERDATABASE;

CREATE TABLE IF NOT EXISTS dishes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

-- Run this seed section only once to avoid duplicate sample rows.
INSERT INTO dishes (name, price, available) VALUES
('Masala Dosa', 80.00, TRUE),
('Veg Sandwich', 60.00, TRUE),
('Cold Coffee', 50.00, TRUE),
('Idli Sambar', 45.00, TRUE);
