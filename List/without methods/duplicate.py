list = [1, 2, 1, 3, 4]
unique = []

print("Original list:", list)
for item in list:
	if item not in unique:
		unique.append(item)

list = unique
print("List after removing duplicates:",  list)
