def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()