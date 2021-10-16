
from sql_alchemy.models import Student

student = Student(
    id=1,
    full_name="Christopher Tumenas"
)


def hello_word(self=student):
    print(self.full_name)

student.hello_word = hello_word
# print(student.id, student.full_name)

student.hello_word()