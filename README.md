# 🍕 Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and the relationship between them — built with Flask, SQLAlchemy, and Flask-Migrate.

---

## 👤 Created by: Boniface Mburu

---

## 📁 Project Structure (MVC)

```
pizza-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 1. Install dependencies & activate virtual environment

```bash
pipenv install
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

### 🧱 2. Database setup and migrations

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```



## 🛣 API Routes Summary

### 📍 `/restaurants`

- **GET** `/restaurants`  
  Returns a list of all restaurants.

- **GET** `/restaurants/<int:id>`  
  Returns a single restaurant with its pizzas.  
  Returns `404` if not found.

- **DELETE** `/restaurants/<int:id>`  
  Deletes the restaurant and all associated `RestaurantPizzas`.  
  Returns `204` if successful or `404` if not found.

---

### 📍 `/pizzas`

- **GET** `/pizzas`  
  Returns a list of all pizzas.

---

### 📍 `/restaurant_pizzas`

- **POST** `/restaurant_pizzas`  
  Creates a new relationship between a pizza and a restaurant.  

#### Request Body:
```json
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

#### Success Response:
```json
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Cheese, Tomato Sauce, Pepperoni"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Palace",
    "address": "123 Flavor St"
  }
}
```

#### Error Response:
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## ✅ Validation Rules

- `price` in `RestaurantPizza` must be between **1 and 30**.
- If invalid, returns status `400` with JSON errors.

---

## 🧪 Testing with Postman

### 📥 Import the Collection

1. Open Postman.
2. Click **Import**.
3. Upload `challenge-1-pizzas.postman_collection.json`.

### 🚀 Run Requests

Make sure your Flask server is running:

```bash
flask run
```

Then run the requests from the collection to test:

- GET all restaurants
- GET one restaurant
- DELETE a restaurant
- GET all pizzas
- POST a restaurant_pizza (valid/invalid)

Base URL: `http://127.0.0.1:5000`

---

