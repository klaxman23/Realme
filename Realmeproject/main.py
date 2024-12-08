from fastapi import FastAPI
from typing import List
from models import Student

app = FastAPI()

# In-memory storage for students
students_db = []

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return students_db

@app.get("/students/{roll_no}", response_model=Student)
async def get_student(roll_no: int):
    for student in students_db:
        if student.roll_no == roll_no:
            return student
    return {"error": "Student not found"}

@app.delete("/students/{roll_no}", response_model=dict)
async def delete_student(roll_no: int):
    global students_db
    students_db = [student for student in students_db if student.roll_no != roll_no]
    return {"message": "Student deleted successfully"}