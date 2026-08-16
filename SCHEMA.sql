-- ============================================
-- CampusEats Database Schema
-- Assignment 2 - Question 5
-- ============================================


-- ============================================
-- 1. ACCOUNTS SERVICE
-- ============================================

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Addresses (
    address_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    address_line VARCHAR(255) NOT NULL,
    city VARCHAR(50),
    pincode VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);


-- ============================================
-- 2. CATALOGUE SERVICE
-- ============================================

CREATE TABLE Restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(150)
);

CREATE TABLE MenuItems (
    item_id INT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);


-- ============================================
-- 3. ORDER SERVICE
-- ============================================

CREATE TABLE Carts (
    cart_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    cart_id INT,
    order_status VARCHAR(30) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cart_id) REFERENCES Carts(cart_id)
);

CREATE TABLE OrderItems (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);


-- ============================================
-- 4. PAYMENT SERVICE
-- ============================================

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_status VARCHAR(30) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Refunds (
    refund_id INT PRIMARY KEY,
    transaction_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    refund_status VARCHAR(30) NOT NULL,
    refund_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transaction_id)
        REFERENCES Transactions(transaction_id)
);


-- ============================================
-- 5. DELIVERY SERVICE
-- ============================================

CREATE TABLE Riders (
    rider_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    availability BOOLEAN DEFAULT TRUE
);

CREATE TABLE DeliveryAssignments (
    assignment_id INT PRIMARY KEY,
    rider_id INT NOT NULL,
    order_id INT NOT NULL,
    delivery_status VARCHAR(30) NOT NULL,
    assigned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rider_id) REFERENCES Riders(rider_id)
);


-- ============================================
-- 6. NOTIFICATION SERVICE
-- ============================================

CREATE TABLE MessageLogs (
    message_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_id INT NOT NULL,
    message VARCHAR(255) NOT NULL,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP
);