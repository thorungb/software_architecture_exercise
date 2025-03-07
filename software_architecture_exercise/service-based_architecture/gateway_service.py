import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
USER_SERVICE_URL = "http://localhost:5001"
PRODUCT_SERVICE_URL = "http://localhost:5002"

@app.route('/register_user', methods=['POST'])
def register_user():
    response = requests.post(f"{USER_SERVICE_URL}/register", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/login_user', methods=['POST'])
def login_user():
    response = requests.post(f"{USER_SERVICE_URL}/login", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/add_product', methods=['POST'])
def add_product():
    response = requests.post(f"{PRODUCT_SERVICE_URL}/add_product", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/get_products', methods=['GET'])
def get_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/get_products")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)
