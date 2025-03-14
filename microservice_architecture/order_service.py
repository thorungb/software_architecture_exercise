from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# order_service creates orders and communicates with user_service
# to validate user information before creating a new user

orders = []
order_counter = 1000

USER_SERVICE_URL = "http://localhost:5001/users"
INVENTORY_SERVICE_URL = "http://localhost:5002/inventory"

@app.route("/orders", methods=["POST"])
def create_order():
    global order_counter
    data = request.get_json()

    # check if user exists
    user_response = requests.get(f"{USER_SERVICE_URL}/{data['user_id']}")
    if user_response.status_code != 200:
        return jsonify({"message": "User not found"}), 404

    # check if product is available
    inventory_response = requests.get(f"{INVENTORY_SERVICE_URL}/{data['product_id']}")
    if inventory_response.status_code != 200:
        return jsonify({"message": "Product unavailable"}), 400

    # check if quantity is available
    requests.post(f"{INVENTORY_SERVICE_URL}/{data['product_id']}", json={"quantity": data["quantity"]})

    order_counter += 1
    order = {
        "order_id": order_counter,
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "quantity": data["quantity"]
    }
    orders.append(order)

    return jsonify({"message": "Order created", "order_id": order_counter})

if __name__ == "__main__":
    app.run(port=5003, debug=True)
