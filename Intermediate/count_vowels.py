vol = input("Enter a string: ")
vcount = 0

for ch in vol:
    if ch in "aeiouAEIOU":
        vcount = vcount + 1

print(vcount)
