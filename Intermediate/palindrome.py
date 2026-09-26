number = int(input("Enter a number: "))
original = str(number)

if original == original[::-1]:
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")
