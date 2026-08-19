
numbers = (10, 20, 30, 40, 50)  # 1. Create a tuple with 5 numbers.
print("Tuple:", numbers)

print("Third element:", numbers[2]) # 2. Access the third element in a tuple.

a, b, c, d, e = numbers  # 3. Unpack a tuple into separate variables.
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
print("e: ", e)


fruits = {"Apple", "Pear", "Mango", "Berry", "Kiwi"} # 4. Create a set of 5 fruits.
print("Fruit set:", fruits)

fruits.add("Banana")  # 5. Add a new fruit to the set.
print("After adding a fruit:", fruits)

fruits.remove("Banana")  # 6. Remove an element from a set.
print("After removing a fruit:", fruits)


set1 = {1, 2, 3, 4} 
set2 = {6, 4, 5, 3}

union_set = set1.union(set2)   # 7. Find union of two sets.
print("Union of 2 Sets: ", union_set)

intersection_set = set1.intersection(set2) # 8. Find intersection of two sets.
print("Intersection of 2 Sets: ", intersection_set)


set1 = {1, 2}      # 9. Check if one set is a subset of another.
set2 = {1, 2, 3, 4, 5}

print("Set1 a subset of set2?", set1.issubset(set2))


numbers = [10, 20, 10, 30, 20, 40, 30]   # 10. Convert a list with duplicate values into a set to remove duplicates.
print("List: ", numbers)
unique_numbers = set(numbers)
print("After removing duplicates:", unique_numbers)


students = {             # 11. Create a dictionary storing student names and marks.
    "Jeny": 85,
    "Aeny": 78,
    "Feny": 92,
    "Keny": 88
}
print("Student marks:", students)

students["Seni"] = 90  # 12. Add a new key-value pair to an existing dictionary.
print("After adding a student:", students)


del students["Seni"]  # 13. Delete a key-value pair from a dictionary.
print("After deleting a student:", students)


dict1 = {               # 14. Merge two dictionaries into one.
    "name": "Jeny",
    "age": 22
}

dict2 = {
    "city": "Chikhli",
    "course": "Python"
}
merged_dict = dict1 | dict2                      #merge (|)
print("Merged dictionary: ", merged_dict)


key = input("Enter a student name to search: ")     # 15. Check if a key exists in a dictionary.

if key in students:
    print("Key exists in the Dictionary!")
else:
    print("Key does not exist in the Dictionary!")


sentence = input("Enter a sentence: ")      # 16. Count word frequency in a given string using a dictionary.
words = sentence.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency in the sentence: ", frequency)


marks = {            # 17. Find the key with the maximum value in a dictionary.
    "Jeny": 85,
    "Aeny": 78,
    "Feny": 92,
    "Keny": 88
}

maximum_key = max(marks, key=marks.get)

print("Student with maximum marks: ", maximum_key)
print("And Maximum marks: ", marks[maximum_key])


original = {   # 18. Reverse keys and values in a dictionary.
    "a": 1,
    "b": 2,
    "c": 3
}
print("Original dictionary:", original)
reversed_dict = {value: key for key, value in original.items()}
print("Reversed dictionary:", reversed_dict)


students["Jeny"] = 95       # 19. Update the value for a specific key.
print("Updated (Student) dictionary:", students)


student_data = [            # 20. Convert a list of tuples into a dictionary.
    ("Jeny", 85),
    ("Aeny", 78),
    ("Feny", 92)
]
student_dict = dict(student_data)
print("Dictionary:", student_dict)