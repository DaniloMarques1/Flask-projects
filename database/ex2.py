from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost/Students"

db = SQLAlchemy(app)

class Student(db.Model):
    id_student = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

def insert_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()

def search_student_by_id(id_student):
    student = Student.query.filter_by(id_student=id_student).first()
    return student

def show_all_students():
    students = Student.query.all()
    return students

def delete_student_by_id(id_student):
    student = Student.query.filter_by(id_student=id_student).first()
    db.session.delete(student)
    db.session.commit()

def update_student(id_student, name):
    student = Student.query.filter_by(id_student=id_student).first()
    if name is not None:
        student.name = name
    db.session.commit()

def main():
    print("Qual operação deseja realizar? ")
    print("1- Inserir um novo estudante: ")
    print("2- Buscar um estudante: ")
    print("3- Exibir todos os estudantes: ")
    print("4- Deletar um estudante: ")
    print("5- Atualizar informações sobre um estudante ")
    option = int(input())
    if option == 1:
        name = input("Nome do estudante: ")
        insert_student(name)
    elif option == 2:
        id = int(input("Id do estudante buscado: "))
        student = search_student_by_id(id)
        print(student.name)
    elif option == 3:
        students = show_all_students()
        for student in students:
            print(student.name)
    elif option == 4:
        id = int(input("Id do usuario a ser deletado: "))
        delete_student_by_id(id)
    elif option == 5:
        id = int(input("Id do usuario que deseja alterar: "))
        new_name = input("Novo nome: ")
        update_student(id, new_name)
if __name__ == "__main__":
    main()
