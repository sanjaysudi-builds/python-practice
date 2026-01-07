# Python program to:
1)Access the first element and the last element of the tuple

2)Slice the tuple to get the middle three elements

3)Concatenate this tuple with another tuple (60, 70)

4)Use a tuple method to find:
how many times 20 appears
the index of 40

# Tuple program 

numbers = (10, 20, 30, 40, 50)
print("First element: ", numbers[0])
print("Second element: ", numbers[-1])

middle_elements = numbers[1:4]
print(middle_elements)

new_tuple = numbers + (60, 70)
print("After concatenation: ", new_tuple)

print("Count of 20: ", numbers.count(20))
print("Index of 40: ", numbers.index(40))



