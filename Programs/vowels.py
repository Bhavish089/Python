text = input("Enter a string: ")
vowels = "aeiouAEIOU"

print("Vowels:", end=" ")
for character in text:
    if character.lower() in vowels:
        print(character, end=" ")
print()
