n = int(input())
grids = [list(map(int, input().split())) for _ in range(n)]

answer = -1

for row in range(n):
    for col in range(n-2):
        for n_row in range(n):
            for n_col in range(n-2):
                # 겹치는 구간
                if row == n_row and abs(col - n_col) <= 2: 
                    continue

                else:
                    section_1 = sum(grids[row][col:col+3])
                    section_2 = sum(grids[n_row][n_col:n_col+3])
                    answer = max(answer, section_1+section_2)

print(answer)