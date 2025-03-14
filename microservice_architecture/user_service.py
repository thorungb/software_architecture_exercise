from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  # collection of users

# user_service handles user creation and retrieval

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"]}
    return jsonify({"message": "User created", "user_id": user_id})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(port=5001, debug=True)
