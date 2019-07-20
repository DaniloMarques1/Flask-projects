from flask import Flask, make_response, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = [{
      "id":1,
      "name":"Danilo Marques",
      "email":"danilomarques20@hotmail.com"
   },
   {
      "id":2,
      "name":"Danilo Marques",
      "email":"danilomarques20@hotmail.com"
   },
   {
      "id":3,
      "name":"Danilo Marques",
      "email":"danilomarques20@hotmail.com"
   }
]

class User(Resource):
    def get(self, id_user):
        for user in users:
            if user["id"] == id_user:
                return make_response(user, 200)
        return make_response({"message" : "User not found it"}, 404)

class Users(Resource):
    def get(self):
        return make_response(jsonify(users), 200)

class AddUser(Resource):
    def post(self):
        last_id = users[len(users) - 1]["id"]
        name = request.json.get("name")
        email = request.json.get("email")
        new_user = {"id" : last_id + 1, "name" : name, "email" : email }
        users.append(new_user)
        return make_response(jsonify(users), 200)


api.add_resource(User, "/user/<int:id_user>")
api.add_resource(Users, "/users")
api.add_resource(AddUser, "/addUser")

if __name__ == "__main__":
    app.run(debug=True)
