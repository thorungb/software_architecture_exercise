from flask import Flask, request, jsonify

app = Flask(__name__)

# inventory_service checks the availability of products

inventory = {
    100: {"product_id": 100, "stock": 10},
    200: {"product_id": 200, "stock": 5}
}

@app.route("/inventory/<int:product_id>", methods=["GET"])
def check_stock(product_id):
    product = inventory.get(product_id)
    if product and product["stock"] > 0:
        return jsonify({"message": "Product available", "stock": product["stock"]})
    return jsonify({"message": "Out of stock"}), 400

@app.route("/inventory/<int:product_id>", methods=["POST"])
def update_stock(product_id):
    data = request.get_json()
    if product_id in inventory:
        inventory[product_id]["stock"] -= data["quantity"]
        return jsonify({"message": "Stock updated", "new_stock": inventory[product_id]["stock"]})
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(port=5002, debug=True)
