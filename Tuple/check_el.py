tup = (1, 2, 3, 4, 5)
element = int(input("Enter an element to check if it exists in the tuple: "))

if element in tup:
    print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")
