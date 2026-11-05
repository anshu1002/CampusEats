
const express = require('express');

const app = express();
const PORT = 4000;

// JSON data read karne ke liye
app.use(express.json());

// Frontend files serve karne ke liye
app.use(express.static('public'));

// In-memory data: 4 seed records
let items = [
    { id: 1, name: 'Burger', price: 80, available: true },
    { id: 2, name: 'Pizza', price: 150, available: true },
    { id: 3, name: 'Sandwich', price: 60, available: true },
    { id: 4, name: 'Cold Coffee', price: 70, available: false }
];

let nextId = 5;

// GET: saare items
app.get('/items', (req, res) => {
    res.status(200).json(items);
});

// GET: ek item by ID
app.get('/items/:id', (req, res) => {
    const id = Number(req.params.id);
    const item = items.find(item => item.id === id);

    if (!item) {
        return res.status(404).json({ error: 'Item not found' });
    }

    res.status(200).json(item);
});

// POST: naya item create karna
app.post('/items', (req, res) => {
    const { name, price } = req.body;

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

    if (!Number.isFinite(newItem.price) || newItem.price < 0) {
        return res.status(422).json({
            error: 'Price must be a valid non-negative number'
        });
    }

    items.push(newItem);
    res.status(201).json(newItem);
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
