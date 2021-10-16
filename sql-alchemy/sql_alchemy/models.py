from sql_alchemy.database import Database

db = Database().get_db()

class Student(db.Model):
    __table_name__ = 'student'
    id = db.Column('id', db.Integer, primary_key=True)
    full_name = db.Column('full_name', db.Unicode)
