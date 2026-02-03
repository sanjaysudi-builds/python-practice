# ==============================
# PYTHON OPERATORS PRACTICE
# ==============================

# 1. Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("--------------------")

# 2. Comparison operators
x = 5
y = 10
print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)

print("--------------------")

# 3. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("--------------------")

# 4. Logical operators
a = 10
b = 20
print("a > 5 and b > 15:", a > 5 and b > 15)
print("a > 15 or b > 15:", a > 15 or b > 15)
print("not(a > 5):", not(a > 5))

print("--------------------")

# 5. Assignment operators
x = 10
x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

print("--------------------")

# 6. Membership operators
text = "Python Programming"
print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)

print("--------------------")

# 7. Identity operators
a = 5
b = 5
print("a is b:", a is b)
print("a is not b:", a is not b)

print("--------------------")

# 8. Compare two strings
s1 = "apple"
s2 = "banana"
print("s1 == s2:", s1 == s2)
print("s1 < s2:", s1 < s2)

print("--------------------")

# 9. Positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("--------------------")

# 10. Use all operators together
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Equal:", a == b)
print("a > 0 and b > 0:", a > 0 and b > 0)