numbers = [8,1,2,3,4,5,6,7,1,9]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest element:", unique_numbers[-2])
else:
    print("List must contain at least two unique elements.")
    