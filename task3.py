
# 1. Take a string input and print its length.

text = input("Enter a string: ")
print("Length of the string: ", len(text))

# 2. Convert a sentence to lowercase.

print("Lowercase:", text.lower())

# 3. Replace spaces with underscores in a string.

result = text.replace(" ", "_")
print("Replacing spaces with underscores :", result)

# 4. Extract the first and last character of a string.

print("First character:", text[0])
print("Last character:", text[-1])

# 5. Reverse a string using slicing.

reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# 6. Count how many times a letter appears in a string.

letter = input("Enter a letter to count: ")
count = text.count(letter)
print("Number of times the letter appears:", count)

# 7. Check if a word is present in a sentence.


word = input("Enter a word to search: ")

if word in text:
    print("Word is present in the sentence.")
else:
    print("Word is not present in the sentence.")

# 8. Take name & age and print using f-string formatting.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Name: {name} and Age: {age}")


# 9. Remove extra spaces from the start and end of a string.

text = input("Enter String with Extra Spaces (in the begining and the end): ")
result = text.strip()
print("Removing Extra Spaces (from the begining and the end): ", result)


# 10. Join a list of words into a single string with - between them.

words = ["Hiii", "Helloo", "How", "are", "you??"]
result = "-".join(words)
print("Joined String:", result)


# 11. Create a list of your 5 favorite movies.

movies = ["Uri", "Dhurandar", "Airlift", "Shershaah", "War"]
print("Favorite Movies: ", movies)


# 12. Add a new movie to the list.

movies.append("Dhurandar 2")
print("After adding a movie: ", movies)


# 13. Remove the first movie from the list.

movies.pop(0)
print("After removing the first movie: ", movies)


# 14. Sort a list of numbers in ascending order.

numbers = [50, 10, 40, 20, 30]
numbers.sort()

print("Sorted Number List: ", numbers)


# 15. Reverse a list.

numbers.reverse()
print("Reversed List: ", numbers)


# 16. Find the largest number in a list.

largest = max(numbers)
print("Largest Number: ", largest)


# 17. Merge two lists into one.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list: ", merged_list)


# 18. Access the last element of a list without using index number.

last_element = numbers.pop()
print("Last element:", last_element)


# 19. Create a nested list and access a specific inner element.

nested_list = [
    ["Name","Email", "Number"],["Marks","Percentage"],["Age", "Address"]
]   
print(nested_list)
print("Specific Inner Element:", nested_list[1][0])


# 20. Count how many times an element appears in a list.

nums = [10, 20, 10, 30, 10, 40, 10]
count = nums.count(10)
print("10 Appearance: ", count)