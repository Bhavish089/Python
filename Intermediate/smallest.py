numbers = [8, 3, 5, 1, 6]

if not numbers:
    print("The list is empty.")
else:
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    print("Smallest element:", smallest)
