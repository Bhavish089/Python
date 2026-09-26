text = input("Enter a string: ")
normalized_text = "".join(character.lower() for character in text if character.isalnum())

if normalized_text == normalized_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")