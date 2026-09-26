start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for number in range(max(2, start), end + 1):
    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)