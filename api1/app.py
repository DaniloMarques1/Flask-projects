from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

users = [
        {
            "id" : 1,
            "name" : "Danilo Marques",
            "email" : "danilomarques20@hotmail.com"
        },
        {
            "id" : 2,
            "name" : "Danilo Marques",
            "email" : "danilomarques20@hotmail.com"
        },
        {
            "id" : 3,
            "name" : "Danilo Marques",
            "email" : "danilomarques20@hotmail.com"
        }
]

@app.route("/user/<int:id_user>")
def user(id_user):
    for user in users:
        if user["id"] == id_user:
            return jsonify(user), 200
    return jsonify({"message" : "User not found it"}), 404

#explicitamente definindo que é uma rota get
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/addUser", methods=["POST"])
def add_user():
    content = request.json
    name = content["name"]
    email = content["email"]
    last_id = users[len(users) - 1]["id"]
    new_user = {"id" : last_id + 1, "name" : content["name"],"email" : content["email"] }
    users.append(new_user)
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)
