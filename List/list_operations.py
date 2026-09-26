# in python we have the concept of the list not array and adding data type is not required

data = [10, "Python", 3.14, True, [1,2,3]]
print(type(data))
print("List name data: ", data)

numbers = [10,20,30,40]
print("\nOriginal List of numbers: ",numbers)

numbers.append(50)
print("\nappend(50): ",numbers)

numbers.extend([60,70])
print("extend([60, 70]): ", numbers)

numbers.insert(1,15)
print("insert(1, 15): ", numbers)

numbers.remove(20)
print("remove(20): ", numbers)

remove = numbers.pop(3)
print("pop(3) value 40 at index 3: ", numbers)
print("Removed value 40 at index 3: ", numbers)

numbers.clear()
print("number list clear(): ", numbers)

numbers = [10,20,30,40]
position = numbers.index(30)
print("index(30): ", position)

count = numbers.count(20)
print("count(): ", count)

numbers.sort()
print("sort(): ", numbers)

numbers.reverse()
print("reverse(): ", numbers)

print("highest value number:", max(numbers))
print("lowest value number: ", min(numbers))