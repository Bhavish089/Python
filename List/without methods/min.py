nums = [8,2,3,1,3]

imin = nums[0]

for num in nums:
    if num < imin:
        imin = num

print(imin)
