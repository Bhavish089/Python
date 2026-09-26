list = [1,2,3,4,5]
print(list)

user_req = int(input("what you want to search in list: "))

if user_req in list:
    print("found: ", user_req)
else:
    print("not found: ", user_req)