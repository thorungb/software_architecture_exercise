from flask import Flask, request, jsonify

app = Flask(__name__)
products = []

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    product_id = data.get('product_id')
    product_name = data.get('product_name')

    products.append({'product_id': product_id, 'product_name': product_name})
    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/get_products', methods=['GET'])
def get_products():
    return jsonify({'products': products}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)
