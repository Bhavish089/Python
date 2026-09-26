terms = int(input("Enter the number of terms: "))
first = 0
second = 1

for _ in range(terms):
    print(first)
    first, second = second, first + second
