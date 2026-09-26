text = input("Enter a string: ")
vowels = "aeiou"
count = 0

for character in text.lower():
    if character.isalpha() and character not in vowels:
        count += 1

print("Number of consonants:", count)
