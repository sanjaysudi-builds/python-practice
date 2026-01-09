*Basic `if` statement*
python
age = 20  
if age >= 18:  
    print("You are eligible to vote")

 Checks if age is 18 or more. Prints "You are eligible to vote"

 *`if-else` example*  
python
age = 16  
if age >= 18:  
    print("Eligible to vote")  
else:  
    print("Not eligible")

Age is 16, so it prints "Not eligible"

 *`elif` for multiple conditions*  

python
marks = 72  
if marks >= 90:  
    print("Grade A")  
elif marks >= 75:  
    print("Grade B")  
elif marks >= 60:  
    print("Grade C")  
else:  
    print("Fail")

 Marks = 72, so it matches `>= 60` and prints "Grade C"

