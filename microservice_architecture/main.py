import requests

ORDER_SERVICE_URL = "http://localhost:5003/orders"
USER_SERVICE_URL = "http://localhost:5001/users"

# HOW TO RUN
# 1. Run user_service.py
# 2. Run inventory_service.py
# 3. Run order_service.py
# 4. Run main.py

# create new user
user_response = requests.post(USER_SERVICE_URL, json={"name": "Alice"})
user_id = user_response.json().get("user_id")
print("User Created:", user_response.json())

# Create order
order_response = requests.post(ORDER_SERVICE_URL, json={
    "user_id": user_id,
    "product_id": 100,
    "quantity": 2
})
print("Order Response:", order_response.json())

# Create order with out of stock product
order_response = requests.post(ORDER_SERVICE_URL, json={
    "user_id": user_id,
    "product_id": 200,
    "quantity": 10
})
print("Order Response (Out of Stock):", order_response.json())

# Create order with invalid user
order_response = requests.post(ORDER_SERVICE_URL, json={
    "user_id": 999,
    "product_id": 100,
    "quantity": 1
})
print("Order Response (Invalid User):", order_response.json())

# Create order with invalid product
order_response = requests.post(ORDER_SERVICE_URL, json={
    "user_id": user_id,
    "product_id": 999,
    "quantity": 1
})
print("Order Response (Invalid Product):", order_response.json())
