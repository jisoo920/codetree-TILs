n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

MAX = max(nums)

def count_len(min_n, max_n):
    cnt = 0

    for num in nums:
        if num >= min_n and num <= max_n:
            cnt += 1
    
    return cnt

ans = 0

for i in range(1, MAX+1):
    max_num = i + k

    ans = max(ans, count_len(i, max_num))

print(ans)