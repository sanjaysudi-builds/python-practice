# ==============================
# PYTHON DATA TYPES PRACTICE
# ==============================

# 1. Variables with different data types
x = 2                # int
y = "krishna"        # str
z = 5.0              # float
accepted = True      # bool

print(x)
print(y)
print(z)
print(accepted)

print("--------------------")

# 2. Print data types
print(type(x))
print(type(y))
print(type(z))
print(type(accepted))

print("--------------------")

# 3. Take number input and print value & type
num = int(input("Enter a number: "))
print(num)
print(type(num))

print("--------------------")

# 4. Convert int to float and string
n = int(input("Enter an integer: "))
print(n, type(n))
print(float(n), type(float(n)))
print(str(n), type(str(n)))

print("--------------------")

# 5. Convert string number to integer
s = input("Enter a string number: ")
print(int(s), type(int(s)))

print("--------------------")

# 6. Add int and float, print result and type
a = 5        # int
b = 2.5      # float
result = a + b
print(result)
print(type(result))

print("--------------------")

# 7. List and its data type
my_list = [10, 20, 30, 40, 50]
print(my_list)
print(type(my_list))

print("--------------------")

# 8. Tuple and its data type
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)
print(type(my_tuple))

print("--------------------")

# 9. Dictionary and its data type
dishes = {
    "Bengalore": "bisi bele bath",
    "Mysore": "mysore pak",
    "Hubballi": "kadak rotti"
}
print(dishes)
print(type(dishes))

print("--------------------")

# 10. Type casting demonstration
# string -> int
s1 = "25"
i1 = int(s1)
print(i1, type(i1))

# int -> float
i2 = 10
f2 = float(i2)
print(f2, type(f2))

# float -> string
f3 = 3.5
s3 = str(f3)
print(s3, type(s3))