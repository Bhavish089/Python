tup = (1, 2, 3, 4, 5)
print(tup)

user = int(input("enter the number to find it's index value: "))

if user in tup:
    print("found value index at:", tup.index(user))
else:
    print("not found", user ,"at tuple")
