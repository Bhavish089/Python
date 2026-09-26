numbers = [10, 25, 7, 42, 18]

largest = None
for number in numbers:
    if largest is None or number > largest:
        largest = number

if largest is None:
    print("The list is empty.")
else:
    print("Largest element:", largest)
