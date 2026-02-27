# PYTHON TUPLE PRACTICE

# 1. Create a tuple and print it
t = (10, 20, 30, 40)
print(t)

print("--------------------")

# 2. Access elements using index
print("First element:", t[0])
print("Last element:", t[-1])

print("--------------------")

# 3. Find length of a tuple
print("Length:", len(t))

print("--------------------")

# 4. Iterate through a tuple
for item in t:
    print(item)

print("--------------------")

# 5. Check if an element exists
print(20 in t)
print(50 in t)

print("--------------------")

# 6. Tuple slicing
print("Slice (1:3):", t[1:3])

print("--------------------")

# 7. Convert tuple to list
lst = list(t)
print(lst, type(lst))

print("--------------------")

# 8. Count occurrences
t2 = (1, 2, 2, 3, 2, 4)
print("Count of 2:", t2.count(2))

print("--------------------")

# 9. Find index of an element
print("Index of 30:", t.index(30))

print("--------------------")

# 10. Nested tuple
nested = (1, (2, 3), (4, 5))
print(nested)