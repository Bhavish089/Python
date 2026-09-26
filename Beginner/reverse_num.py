number = int(input("Enter a number: "))
sign = -1 if number < 0 else 1
remaining = abs(number)
reversed_number = 0

while remaining > 0:
    reversed_number = reversed_number * 10 + remaining % 10
    remaining //= 10

print("Reversed number:", sign * reversed_number)
