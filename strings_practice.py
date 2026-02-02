# ==============================
# PYTHON STRING PRACTICE
# ==============================

# 1. Create a string and print it
name = "Krishna"
print(name)

print("--------------------")

# 2. Find length of a string
text = "Python Programming"
print("Length:", len(text))

print("--------------------")

# 3. Access first and last character
word = "Python"
print("First character:", word[0])
print("Last character:", word[-1])

print("--------------------")

# 4. Convert string to uppercase and lowercase
msg = "Hello World"
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())

print("--------------------")

# 5. Check whether a word is present in a string
sentence = "I am learning Python"
print("Python" in sentence)

print("--------------------")

# 6. Reverse a string
s = "Python"
print("Reversed string:", s[::-1])

print("--------------------")

# 7. Count number of vowels in a string
string = "education"
vowels = "aeiou"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Vowel count:", count)

print("--------------------")

# 8. Check whether a string is palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

print("--------------------")

# 9. Replace a word in a string
text = "I like Java"
new_text = text.replace("Java", "Python")
print(new_text)

print("--------------------")

# 10. Count characters, words, and spaces
sentence = "Python is easy to learn"

characters = len(sentence)
words = len(sentence.split())
spaces = sentence.count(" ")

print("Characters:", characters)
print("Words:", words)
print("Spaces:", spaces)