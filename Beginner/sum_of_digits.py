number = int(input("Enter a number: "))
remaining = abs(number)
digit_sum = 0

while remaining > 0:
    digit_sum += remaining % 10
    remaining //= 10

print("Sum of digits:", digit_sum)
