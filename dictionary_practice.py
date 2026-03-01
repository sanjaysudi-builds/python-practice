# ==============================
# PYTHON DICTIONARY PRACTICE
# ==============================

# 1. Create a dictionary and print it
student = {
    "name": "Krishna",
    "age": 21,
    "course": "Python"
}
print(student)

print("--------------------")

# 2. Access value using key
print("Name:", student["name"])

print("--------------------")

# 3. Add a new key-value pair
student["city"] = "Bengaluru"
print("After adding city:", student)

print("--------------------")

# 4. Update an existing value
student["age"] = 22
print("After updating age:", student)

print("--------------------")

# 5. Delete a key-value pair
del student["course"]
print("After deleting course:", student)

print("--------------------")

# 6. Print all keys
print("Keys:", student.keys())

print("--------------------")

# 7. Print all values
print("Values:", student.values())

print("--------------------")

# 8. Check if a key exists
print("age" in student)
print("marks" in student)

print("--------------------")

# 9. Count number of keys
print("Total keys:", len(student))

print("--------------------")

# 10. Student with highest marks
marks = {
    "Amit": 78,
    "Ravi": 85,
    "Neha": 92,
    "Sita": 88
}

topper = max(marks, key=marks.get)
print("Topper:", topper)
print("Highest Marks:", marks[topper])