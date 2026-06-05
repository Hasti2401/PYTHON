import timeit

nums = [23,78,54,12,49,30,42,18,6]

n = len(nums)

for i in range(n):
    for j in range(n - i -1):
        
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

print(timeit.timeit(number=1))