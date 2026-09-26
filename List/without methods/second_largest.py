list = [4,1,3,2,5,3,6]
second_largest = 0

for i in range(len(list)):
    if list[i] > second_largest and list[i] < max(list):
        second_largest = list[i]
print("second largest element is: ", second_largest)