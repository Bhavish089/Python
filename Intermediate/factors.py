number = int(input("Enter a positive number: "))

if number <= 0:
    print("Please enter a positive number.")
else:
    print("Factors:")
    for factor in range(1, number + 1):
        if number % factor == 0:
            print(factor)
