text = input("Enter a string: ")
seen = set()
duplicates = []

for character in text:
    if character in seen and character not in duplicates:
        duplicates.append(character)
    else:
        seen.add(character)

if duplicates:
    print("Duplicate characters:", " ".join(duplicates))
else:
    print("No duplicate characters found.")