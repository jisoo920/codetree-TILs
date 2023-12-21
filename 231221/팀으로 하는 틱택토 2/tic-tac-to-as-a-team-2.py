MAX = 10

nums = list()
num_list = set()
for _ in range(3):
    tmp = input()
    nums.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])
    num_list.update([int(tmp[0]), int(tmp[1]), int(tmp[2])])

num_list = list(num_list)

answer = 0

def check_win(grid):
    # 가로
    for g in grid:
        if sum(g) == 3:
            return True

    # 세로
    for c in range(3):
        if grid[0][c] + grid[1][c] + grid[2][c] == 3:
            return True

    # 대각선
    if grid[0][0] + grid[1][1] + grid[2][2] == 3:
        return True

    # 역대각선
    if grid[0][2] + grid[1][1] + grid[2][0] == 3:
        return True

    return False

for i in range(1, MAX-1):
    if i not in num_list:
        continue
    
    for j in range(i+1, MAX):
        if j not in num_list:
            continue

        grid = [[-1, -1, -1] for _ in range(3)]
        num_cnt = [0]*MAX

        for r in range(3):
            for c in range(3):
                if nums[r][c] == i:
                    grid[r][c] = 1
                    num_cnt[i] += 1

                if nums[r][c] == j:
                    grid[r][c] = 1
                    num_cnt[j] += 1
        
        if check_win(grid):
            if 3 in num_cnt:
                continue
            else:
                answer += 1

print(answer)