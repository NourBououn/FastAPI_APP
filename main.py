from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

#fastapi app creation
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
#ta3rif namouthaj l bayanet
class Student(BaseModel):
    id: int
    name: str
    grade: int
#Liste pour le stockage des données 
students = [
    Student(id=1,name="nour",grade=9),
    Student(id=1,name="oussema",grade=10),
    Student(id=1,name="ali",grade=8),
    Student(id=1,name="mehdi",grade=7),
    Student(id=1,name="asma",grade=6),
]
<<<<<<< HEAD

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Student API!"}

=======
>>>>>>> 89a7a72 (Updated FastAPI app)
#Read all the elements 
@app.get("/students")
def read_student():
    return students

@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
        
    return {"error" : "Student not found"}   
 
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error" : "Student not found"}
        