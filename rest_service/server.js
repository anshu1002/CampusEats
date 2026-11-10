
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const express = require('express');

const app = express();
const PORT = 4000;

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Seed users with bcrypt hashed passwords
const users = [
    {
        id: 1,
        email: 'customer@ampuseats.com',
        passwordHash: '$2b$10$hTdaOheU2rjxi0Vb9Ong1.62rda3CLqGb4ZGDVBmmWSe/7ZQ753s2',
        role: 'customer'
    },
    {
        id: 2,
        email: 'restaurant@campus.com',
        passwordHash: '$2b$10$R/iYP8UrOVhXvz4CCTo2wuFNwP1ZuinxnC6ZgfizD2zcinUpUQQ1u',
        role: 'restaurant'
    }
];

// In-memory items
let items = [
    { id: 1, name: 'Burger', price: 80, available: true },
    { id: 2, name: 'Pizza', price: 150, available: true },
    { id: 3, name: 'Sandwich', price: 60, available: true },
    { id: 4, name: 'Cold Coffee', price: 70, available: false }
];

let nextId = 5;


// POST: User Login
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    // Find user by email
    const user = users.find(user => user.email === email);

    // Check email and password
    if (
        !user ||
        typeof password !== 'string' ||
        !bcrypt.compareSync(password, user.passwordHash)
    ) {
        return res.status(401).json({
            error: 'Invalid email or password'
        });
    }

    // Generate JWT token
    const token = jwt.sign(
        {
            sub: user.id,
            role: user.role
        },
        process.env.JWT_SECRET,
        {
            expiresIn: '1h'
        }
    );

    res.status(200).json({
        message: 'Login successful',
        token: token
    });
});


// Authentication Middleware
function auth(req, res, next) {
    const authHeader = req.headers.authorization;

    // Check Authorization header
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).json({
            error: 'Access token is required'
        });
    }

    const token = authHeader.split(' ')[1];

    try {
        // Verify JWT token
        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        req.user = decoded;

        next();
    } catch (error) {
        return res.status(401).json({
            error: 'Invalid or expired token'
        });
    }
}


// Role-Based Authorization Middleware
function requireRole(...allowedRoles) {
    return (req, res, next) => {

        if (!allowedRoles.includes(req.user.role)) {
            return res.status(403).json({
                error: 'You do not have permission to perform this action'
            });
        }

        next();
    };
}


// GET: Get all items (Authentication Required)
app.get('/items', auth, (req, res) => {
    res.status(200).json(items);
});


// GET: Get item by ID (Authentication Required)
app.get('/items/:id', auth, (req, res) => {
    const id = Number(req.params.id);

    const item = items.find(item => item.id === id);

    if (!item) {
        return res.status(404).json({
            error: 'Item not found'
        });
    }

    res.status(200).json(item);
});


// POST: Create a new item (Restaurant Role Required)
app.post('/items', auth, requireRole('restaurant'), (req, res) => {
    const { name, price } = req.body;

    // Validate input
    if (!name || price === undefined || price === null || price === '') {
        return res.status(422).json({
            error: 'Name and price are required'
        });
    }

    const newItem = {
        id: nextId++,
        name,
        price: Number(price),
        available: true
    };

    // Validate price
    if (!Number.isFinite(newItem.price) || newItem.price < 0) {
        return res.status(422).json({
            error: 'Price must be a valid non-negative number'
        });
    }

    items.push(newItem);

    res.status(201).json(newItem);
});


// Start Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
