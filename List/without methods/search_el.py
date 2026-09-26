list = [1,2,3,4,5]

user_input = int(input("Enter the number to search: "))
for i in range(len(list)):
    if list[i] == user_input:
        print("Element found at index: ", i)
