# Python Exception Handling - Beginner Examples

print("=== Python Exception Handling Examples ===\n")

# 1. ZeroDivisionError
print("1) Division Example")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid number input.")
print("-" * 40)


# 2. ValueError
print("2) Age Checker")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)
print("-" * 40)


# 3. FileNotFoundError
print("3) File Reading Example")
try:
    filename = input("Enter filename to open: ")
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
print("-" * 40)


# 4. IndexError
print("4) List Index Example")
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index number: "))
    print("Value:", numbers[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a number.")
print("-" * 40)


# 5. Custom Exception
print("5) Login System")

class LoginError(Exception):
    pass

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise LoginError("Invalid login credentials")

    print("Login successful!")
except LoginError as e:
    print("Login failed:", e)

print("\n=== Program Finished ===")