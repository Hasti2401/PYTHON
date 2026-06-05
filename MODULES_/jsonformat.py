import json

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

student_data = {
    "Name" : name,
    "Age" : age,
    "City" : city
}

with open("student_data.txt", "x") as f:
    json.dump(student_data, f, indent = 4)
