import requests

gateway_url = "http://localhost:5000"

def test_register_user():
    url = f"{gateway_url}/register_user"
    data = {"username": "john_doe", "password": "1234"}
    response = requests.post(url, json=data)
    print("Register User Response:", response.json())

def test_login_user():
    url = f"{gateway_url}/login_user"
    data = {"username": "john_doe", "password": "1234"}
    response = requests.post(url, json=data)
    print("Login User Response:", response.json())

def test_add_product():
    url = f"{gateway_url}/add_product"
    data = {"product_id": "1", "product_name": "Laptop"}
    response = requests.post(url, json=data)
    print("Add Product Response:", response.json())

def test_get_products():
    url = f"{gateway_url}/get_products"
    response = requests.get(url)
    print("Get Products Response:", response.json())

def run_tests():
    print("Starting API Tests...")
    test_register_user()
    test_login_user()
    test_add_product()
    test_get_products()
    print("All tests completed!")

if __name__ == "__main__":
    run_tests()