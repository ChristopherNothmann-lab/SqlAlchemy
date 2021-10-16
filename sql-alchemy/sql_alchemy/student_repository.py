from sql_alchemy.database import Database
from sql_alchemy.models import Student

db = Database().get_db()

class StudentRepository:

    def insert_new_student(self, student: Student) -> None:
        db.session.add(student)
        db .session.commit()

    def get_student_from_name(self, full_name: str) -> Student:
        print(type(Student.query.filter_by(full_name=full_name)))
        student = Student.query.filter_by(full_name=full_name).first()
        return student 

    def update_student(self, student: Student) -> None:
    # student.full_name = 'Christopher Tumenas'
        db.session.add(student)
        db.session.commit()

    def delete_student(self, student: Student) -> None:
        db.session.delete(student)
        db.session.commit()
