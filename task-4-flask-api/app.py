from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_users():
    data = request.json

    if isinstance(data, list):
        for user in data:
            user_id = user.get("id")
            name = user.get("name")
            if not user_id or not name:
                continue  # Skip invalid entries
            users[user_id] = {"name": name}
        return jsonify({"message": "Users added"}), 201

    # Handle single user as fallback
    user_id = data.get("id")
    name = data.get("name")
    if not user_id or not name:
        return jsonify({"error": "Missing 'id' or 'name'"}), 400
    users[user_id] = {"name": name}
    return jsonify({"message": "User added"}), 201


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Missing 'name'"}), 400

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users[user_id]["name"] = name
    return jsonify({"message": "User updated"}), 200




@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

@app.route('/')
def home():
    return "<h1>Welcome to the User API</h1>"


if __name__ == '__main__':
    app.run(debug=True)
