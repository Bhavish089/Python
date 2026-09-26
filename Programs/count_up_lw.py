text = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0

for character in text:
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1

print("Uppercase characters:", uppercase_count)
print("Lowercase characters:", lowercase_count)
