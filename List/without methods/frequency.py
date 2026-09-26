list = [1, 2, 8, 3, 2, 2, 8, 5, 1]
traversed = [False] * len(list)

for i in range(len(list)):
    if traversed[i]:
        continue

    count = 1
    
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            traversed[j] = True
            count += 1

    print(f"Element {list[i]} appears {count} time")