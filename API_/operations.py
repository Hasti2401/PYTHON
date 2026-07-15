students = [
    {"id" : 1, "name" : "Hasti", "Course" : "Python"},
    {"id" : 2, "name" : "Riya", "Course" : "Java"}
]

# GET
def get_students():
    return students

#GET BY ID
def get_student(student_id):
    for student in students:
        if ["id"] == student_id:
            return student
    return{"message": "Student not found"}

#POST
def add_student(student):
    students.append(student)
    return {"message": "Student Added Successfully"}

#PUT
def update_student(student_id,updated_student):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = update_student
            return{"message" : "Student updated successfully"}
    return{"message": "Student not found"}

#DELETE
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return{"message": "Student Deleted successfully"}
    return{"message": "Student not found"}