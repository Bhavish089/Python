text = input("Enter a string: ")
seen = set()
repeated_character = None

for character in text:
    if character in seen:
        repeated_character = character
        break
    seen.add(character)

if repeated_character is None:
    print("No character appears twice.")
else:
    print("First character that appears twice:", repeated_character)
    