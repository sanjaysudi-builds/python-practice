# PYTHON LIST PRACTICE

# 1. Create a list and print it
numbers = [10, 20, 30, 40, 50]
print(numbers)

print("--------------------")

# 2. Access elements from a list
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("--------------------")

# 3. Add an element to a list
numbers.append(60)
print("After append:", numbers)

print("--------------------")

# 4. Insert an element at a specific position
numbers.insert(2, 25)
print("After insert:", numbers)

print("--------------------")

# 5. Remove an element from a list
numbers.remove(40)
print("After remove:", numbers)

print("--------------------")

# 6. Find length of a list
print("Length of list:", len(numbers))

print("--------------------")

# 7. Sort a list
numbers.sort()
print("Sorted list:", numbers)

print("--------------------")

# 8. Reverse a list
numbers.reverse()
print("Reversed list:", numbers)

print("--------------------")

# 9. Find maximum and minimum
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

print("--------------------")

# 10. Remove duplicate elements from a list
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(dup_list))
print("Original list:", dup_list)
print("Without duplicates:", unique_list)