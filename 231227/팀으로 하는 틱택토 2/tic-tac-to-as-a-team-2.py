MAX = 10

nums = list()
for _ in range(3):
    tmp = input()
    nums.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])

answer = 0

def check_win(grid):
    # 가로
    for r in range(3):
        num_list = [grid[r][0], grid[r][1], grid[r][2]]
        if (0 not in num_list) and len(set(num_list)) == 2 :
            return True

    # 세로
    for c in range(3):
        num_list = [grid[0][c], grid[1][c], grid[2][c]]
        if (0 not in num_list) and len(set(num_list)) == 2 :
            return True

    # 대각선
    num_list = [grid[0][0], grid[1][1], grid[2][2]]
    if (0 not in num_list) and len(set(num_list)) == 2 :
        return True

    # 역대각선
    num_list = [grid[0][2], grid[1][1], grid[2][0]]
    if (0 not in num_list) and len(set(num_list)) == 2 :
        return True

    return False

for i in range(1, MAX-1):
    for j in range(i+1, MAX):
        grid = [[0, 0, 0] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                if nums[r][c] == i:
                    grid[r][c] = i

                if nums[r][c] == j:
                    grid[r][c] = j
    
        if check_win(grid):
            answer += 1

                

print(answer)