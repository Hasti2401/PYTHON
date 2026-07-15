from fastapi import FastAPI
from pydantic import BaseModel

from operations import(
    get_students,
    get_student,
    add_student,
    update_student,
    delete_student
)

app = FastAPI()

class Student(BaseModel):
    id : int
    name : str
    course : str

@app.get("/students")
def read_students():
    return get_students()

@app.get("/studnets/{student_id}")
def read_student(student_id: int):
    return get_student(student_id)

@app.post("/students")
def create_student(student : Student):
    return add_student(student.dict())

@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    return update_student(student_id, student.dict())

@app.delete("/students/{student_id}")
def remove_studnet(student_id: int):
    return delete_student(student_id)