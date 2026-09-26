num = [-3,-2,-1,0,1,2,3]

pve = [x for x in num if x < 0]
nve = [ x for x in num if x > 0]
zero = [x for x in num if x == 0]

print("Positives:", pve)
print("Negatives:", nve)
print("Zeros:", zero)
