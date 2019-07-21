from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource, Api

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "thisissupersecret"

jwt = JWTManager(app)
api = Api(app)



class Login(Resource):
	def post(self):
		email = request.json.get("email")
		password = request.json.get("password")
		if email == "danilomarques20@hotmail.com" and password == "1234":
			#identity que será retornado quando acessar a rota /user com um token valido (token gerado com esse login)
			user = {"id" : 1, "name" : "Danilo Marques", "email" : "danilomarques20@hotmail.com"}
			token = create_access_token(identity=user)
			return make_response({"access_token" : token}, 200)
		else:
			return make_response({"message" : "Invalid credentials"}, 400)


class User(Resource):
	@jwt_required
	def get(self):
		return make_response(get_jwt_identity(), 200)

#endpoint para geração do token
api.add_resource(Login, "/login")

#endpoint para recuperar o usuario logado
api.add_resource(User, "/user")

#decorator para mudar o comportamento padrão do token inválido caso tenha sido expirado
@jwt.expired_token_loader
def expired_token_loader(expired_token):
	token_type = expire_token["type"]
	return jsonify({"message" : "Invalid token"}), 401

#muda o comportamento do token caso o mesmo seja inválido
@jwt.invalid_token_loader
def invalid_token_loader(token):
	return jsonify({"message" : "Invalid token"}), 401

if __name__ == "__main__":
	app.run(debug=True)