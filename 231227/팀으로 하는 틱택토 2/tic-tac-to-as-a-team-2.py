MAX = 10

nums = list()
for _ in range(3):
    tmp = input()
    nums.append([int(tmp[0]), int(tmp[1]), int(tmp[2])])

answer = 0

def check_win(grid):
    # 가로
    for r in range(3):
        if 0 not in [grid[r][0], grid[r][1], grid[r][2]]:
            return True, set([grid[r][0], grid[r][1], grid[r][2]])

    # 세로
    for c in range(3):
        if 0 not in [grid[0][c], grid[1][c], grid[2][c]]:
            return True, set([grid[0][c], grid[1][c], grid[2][c]])

    # 대각선
    if 0 not in [grid[0][0], grid[1][1], grid[2][2]]:
        return True, set([grid[0][0], grid[1][1], grid[2][2]])

    # 역대각선
    if 0 not in [grid[0][2], grid[1][1], grid[2][0]]:
        return True, set([grid[0][2], grid[1][1], grid[2][0]])

    return False, set([0])

for i in range(1, MAX-1):
    for j in range(i+1, MAX):
        grid = [[0, 0, 0] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                if nums[r][c] == i:
                    grid[r][c] = i

                if nums[r][c] == j:
                    grid[r][c] = j
        
        checked, num_set = check_win(grid)
        if checked:
            if len(num_set) == 2:
                answer += 1
                

print(answer)