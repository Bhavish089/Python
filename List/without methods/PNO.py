#PNO for Positive - Negative - Zero value in a list
list = [-3, -2, -1, 0, 1, 2, 3]

for element in list:
    if element == 0:
        print("element is zero", element)
    if element > 0:
        print("element is positive", element)
    if element < 0:
        print("element is negative", element)