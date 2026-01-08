python_students = {"Ravi", "Anita", "Suresh", "Meena"}
java_students = {"Suresh", "Meena", "Kiran"}

# Students who like both
intersection_set = python_students & java_students
print("Both Python and Java:", intersection_set)

# Students who like only Python
only_python = python_students - java_students
print("Only Python:", only_python)

# Add a new student
python_students.add("Vinnu")
print("Updated Python Students:", python_students)

# Remove a student
java_students.discard("Suresh")
print("Updated Java Students:", java_students)