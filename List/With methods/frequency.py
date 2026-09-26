num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequencies = {x: num.count(x) for x in set(num)}
print(frequencies, "times")
