n = int(input())
nums = list(map(int, input().split()))

used = [0] *(n+1)

for i in range(1, n):
    success = True
    
    ans_nums = [0] * n
    ans_nums[0] = i
    
    used = [0] * (n+1)

    #print("ans_nums: ", ans_nums)

    for j in range(n-1):
        diff = nums[j] - ans_nums[j]
        
        if diff <= 0 or diff > n:
            success = False
            break
        
        if used[diff] == 1:
            success = False
            break         

        used[diff] = 1
        ans_nums[j+1] = diff
        
        #print("a ans_nums:", ans_nums)
        #print("u used", used)

    if success:
        #print("success")
        print(*ans_nums)
        break