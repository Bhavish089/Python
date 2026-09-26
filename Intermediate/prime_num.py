number = int(input("Enter a number: "))
is_prime = number > 1

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
