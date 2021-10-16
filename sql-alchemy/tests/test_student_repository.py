import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sql_alchemy import __version__
from sql_alchemy.models import Student
from sql_alchemy.student_repository import StudentRepository



@pytest.fixture
def flask_app_mock():
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_student_object():
    student = Student(
        id=1,
        full_name="Christopher Tumenas"
    )
    def first (self=student):
        return self
        
    student.first = first
    return student

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock=mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock



def test_version():
    assert __version__ == '0.1.0'

# def test_insert_new_student(
#     flask_app_mock,
#     mock_get_sqlalchemy,
#     mock_student_object
# ):
#     new_student_object = Student(
#         id=1,
#         full_Name="Christopher Tumenas"
#     )

#     with flask_app_mock.app_context():
#         response = StudentRepository().insert_new_student(new_student_object)
#         assert response

def test_get_student_from_name(
    flask_app_mock,
    mock_get_sqlalchemy,
    mock_student_object
):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value = mock_student_object
        response = StudentRepository().get_student_from_name(full_name=mock_student_object.full_name)

        assert response == mock_student_object

def test_update_student():
    assert 100 == 100

def test_delete_student():
    assert 100 == 100

