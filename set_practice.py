# PYTHON SET PRACTICE
# ==============================

# 1. Create a set and print it
s = {10, 20, 30, 40}
print(s)

print("--------------------")

# 2. Add an element to a set
s.add(50)
print("After add:", s)

print("--------------------")

# 3. Remove an element from a set
s.remove(20)
print("After remove:", s)

print("--------------------")

# 4. Discard an element (no error if missing)
s.discard(100)
print("After discard:", s)

print("--------------------")

# 5. Check membership
print(30 in s)
print(20 in s)

print("--------------------")

# 6. Union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)

print("--------------------")

# 7. Intersection of two sets
print("Intersection:", a & b)

print("--------------------")

# 8. Difference of two sets
print("Difference (a-b):", a - b)

print("--------------------")

# 9. Convert list to set (remove duplicates)
lst = [1, 2, 2, 3, 4, 4, 5]
unique = set(lst)
print("Unique elements:", unique)

print("--------------------")

# 10. Clear a set
unique.clear()
print("After clear:", unique)