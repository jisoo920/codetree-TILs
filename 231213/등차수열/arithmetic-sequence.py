n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

max_diff = int((nums[-1] - nums[0])/2)

max_count = -1

for center in range(nums[0]+1, nums[-1]):
    count = 0

    for k in range(1, max_diff+1):
        if (center-k) in nums and (center+k) in nums:
            count += 1
        
    max_count = max(max_count, count)

print(max_count)