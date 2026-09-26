number = int(input("Enter a positive number: "))
divisor_sum = 0

if number > 1:
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

if number > 0 and divisor_sum == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
