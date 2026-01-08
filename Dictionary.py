python_students = {
    "Ravi": 85,
    "Anita": 90,
    "Suresh": 88,
    "Meena": 92
}

java_students = {
    "Suresh": 80,
    "Meena": 89,
    "Kiran": 75
}

# Common students
common_students = python_students.keys() & java_students.keys()
print("Common students:", common_students)

# Only Python students
only_python = python_students.keys() - java_students.keys()
print("Only Python students:", only_python)

# Add new student
python_students["Vinnu"] = 70
print("Updated Python students:", python_students)

# Remove a student
java_students.pop("Suresh")
print("Updated Java students:", java_students)
