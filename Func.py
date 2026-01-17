# Some fuction programs

# Defining a fuction

def greet():
    print("Hello !  Namaskara")
greet()

# Function parameters 

def marriage(boy_name, girl_name):
    print(f"Boy is {boy_name}")
    print(f"Girl is {girl_name}")
    print(f"{boy_name} married {girl_name}")
    
marriage("kiran" , "kavya")

# Returning values from a fuction

def add_numbers(a,b):
    return a + b
result = add_numbers(10,90)
print("The sum is : ",result)

#Default parameter value 

def greet(name = "Student"):
    print(f"Hello, {name}! ")
greet()
greet("Jon")  # uses passed value "Jon"


    

