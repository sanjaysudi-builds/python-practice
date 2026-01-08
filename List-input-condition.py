Taking 5 numbers from the user, store them in a list, and print:
 1)The complete list
 2) Only the even numbers
 
 nums = []

for i in range(5):
    n = int(input("Enter number: "))
    nums.append(n)

print("List:", nums)

print("Even numbers:")
for num in nums:
    if num % 2 == 0:
        print(num)