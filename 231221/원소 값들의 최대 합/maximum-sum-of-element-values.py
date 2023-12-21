n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

for start in range(n):
    cnt, num_sum = 0, 0
    idx = start
    # move
    for i in range(m):
        num_sum += nums[idx]
        idx = nums[idx]-1
    
    answer = max(answer, num_sum)

print(answer)