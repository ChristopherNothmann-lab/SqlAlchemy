from sql_alchemy.database import Database
from sql_alchemy.models import Student
from sql_alchemy.student_repository import StudentRepository


s = Student(id=1,full_name='Christopher')
r = StudentRepository()


r.insert_new_student(student=s) 