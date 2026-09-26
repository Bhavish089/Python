vol = input("Enter a string: ")

for i in range(len(vol)):
    if(vol[i] in "aeiouAEIOU"):
        vcount = vcount + 1
        print(i , " has a vowel")
    else:
        print("has not a vowel")