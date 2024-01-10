n, k = map(int, input().split())
nums = list(map(int, input().split()))

MAX_N = 100

def is_possible(limit):
    last_idx = 0

    for i in range(1, n):
        if nums[i] <= limit:
            if i-last_idx > k:
                return False
            last_idx = i

    return True


for i in range(max(nums[0], nums[-1]), MAX_N+1):
    if is_possible(i):
        print(i)
        break