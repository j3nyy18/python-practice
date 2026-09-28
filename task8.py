# 1. Write a program to read a file and display its contents.

with open("sample.txt", "r") as file:
    content = file.read()
print("File Contents:")
print(content)


# 2. Write a program to count the number of lines in a file.

with open("sample.txt", "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))


# 3. Write a program to count how many times each word appears in a file.

with open("sample.txt", "r") as file:
    content = file.read()
words = content.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")

for word, count in word_count.items():
    print(word, ":", count)


# 4. Write a program to write 5 user-entered sentences to a file.

with open("sentences.txt", "w") as file:
    for i in range(5):
        sentence = input(f"\nEnter sentence {i + 1}: ")
        file.write(sentence + "\n")
print("5 sentences have been written to the file")


# 5. Write a program to append a list of strings to an existing file.

words_list = ["Python", "Django", "Flask", "FastAPI"]
with open("sentences.txt", "a") as file:
    for word in words_list:
        file.write(word + "\n")
print("Strings have been appended to the file")


# 6. Write a program to read a file and print only lines containing a specific word.

search_word = input("Enter a word to search for: ")
with open("sample.txt", "r") as file:
    for line in file:
        if search_word.lower() in line.lower():
            print(line.strip())


# 7. Write a program to replace a specific word in a file and save changes.

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
with open("sample.txt", "r") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open("sample.txt", "w") as file:
    file.write(content)
print("Word replaced successfully")

# 8. Write a program to merge the contents of two text files into a third file.

with open("file1.txt", "r") as file:
    content1 = file.read()
with open("file2.txt", "r") as file:
    content2 = file.read()
with open("merged.txt", "w") as file:
    file.write(content1)
    file.write("\n")
    file.write(content2)
print("Files merged successfully")

# 9. Write a program to read a CSV file and display its content in a formatted way.

import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Student Details:")
    for row in reader:
        print(
            f"Name: {row['Name']} | "
            f"Age: {row['Age']} | "
            f"Marks: {row['Marks']}"
        )


# 10. Write a program to back up a file by copying its contents into another file.

with open("sample.txt", "r") as source:
    content = source.read()
with open("backup.txt", "w") as backup:
    backup.write(content)
print("Backup created successfully")