text = input("Enter a string: ")
vowels = "aeiou"

print("Consonants:", end=" ")
for character in text:
    if character.isalpha() and character.lower() not in vowels:
        print(character, end=" ")
print()
