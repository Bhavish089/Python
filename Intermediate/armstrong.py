number = int(input("Enter a non-negative integer: "))
digits = str(number)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if number >= 0 and total == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
