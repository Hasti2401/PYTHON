nums = [12,16,90,18,60]

n = len(nums)

for i in range(n):

    for j in range(i+1, n):

        if nums[j] < nums[i]:

            nums[i] , nums[j] = nums[j], nums[i]

print(nums)