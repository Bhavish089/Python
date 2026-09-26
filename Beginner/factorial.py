number = int(input("Enter a non-negative integer: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for value in range(1, number + 1):
        factorial *= value

    print("Factorial:", factorial)
