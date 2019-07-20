from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#caminho do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"]  = "mysql://root:12345@localhost/Empresa"

db  = SQLAlchemy(app)


#empregado
class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40), nullable=False)
	email = db.Column(db.String(40), unique=True, nullable=False,)
	function_id = db.Column(db.Integer, db.ForeignKey("function.id_function"))

#função do empregado
class Function(db.Model):
	id_function = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	salary = db.Column(db.Float, nullable=False)
	employee = db.relationship("Employee", backref="employee", lazy=True)

def add_functions():
	'''
		adicionar funções
	'''
	functions = [{"name" : "Suporte Tecnico",  "salary":2300}, {"name" : "Diretor", "salary" : 4200}, {"name" : "admin", "salary" : 2600}]
	for i in functions:
		f = Function(name=i["name"], salary=i["salary"])
		db.session.add(f)
	db.session.commit()

def add_employee():
	'''
	adiciona functionarios
	'''	
	employee = [{"name" : "Manoel", "email":"Manoel@hotmail.com", "function_id" : 3}, {"name" : "Jean", "email":"Jean@hotmail.com", "function_id" : 1}, {"name" : "Fernando", "email":"fernando@hotmail.com", "function_id" : 4}, {"name" : "José", "email":"jose@hotmail.com", "function_id" : 2}]

	for i in employee:
		e = Employee(username=i["name"], email=i["email"], function_id=i["function_id"])
		db.session.add(e)
	db.session.commit()	

def print_function_employee():
	'''
	imprime a função de um empregado
	'''
	empregado = Employee.query.filter_by(username="Danilo Marques").first()
	print(f"A função do empregado {empregado.username} é {empregado.employee.name}")
	

def print_employee_function():
	'''
	imprime o nome dos empregados de todas as funções
	'''
	functions = Function.query.all()
	for function in functions:
		print(f"Os funcionarios da função {function.name} São:")
		for empregado in function.employee:
			print(empregado.username)
		print()

@app.route("/")
def return_employee_json():
	lista = []
	empregados = Employee.query.all()
	for empregado in empregados:
		lista.append({"name" : empregado.username, "position" : empregado.employee.name})

	return jsonify(lista)


def main():
	pass

if __name__ == "__main__":
	#print_function_employee()
	#print_employee_function()
	#return_employee_json()
	app.run(debug=True)