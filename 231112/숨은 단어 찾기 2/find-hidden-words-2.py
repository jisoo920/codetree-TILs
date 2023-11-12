n, m = map(int, input().split())

str_grids = [list(input()) for _ in range(n)]

drs = [-1, -1, -1, 0, +1, +1, +1, 0]
dcs = [-1, 0, +1, +1, +1, 0, -1, -1]


def is_in_range(r, c):
    return 0 <= r < n and 0 <= c < m

answer = 0

for row in range(n):
    for col in range(m):

        if str_grids[row][col] != 'L':
            continue
        
        
        #print("row, col: ", row, col)
        #print("str: ", str_grids[row][col])

        for dr, dc in zip(drs, dcs):
            #print("dr, dc: ", dr, dc)
            n_row, n_col = row, col
            e_cnt = 0

            for idx in range(2):
                n_r = n_row + dr
                n_c = n_col + dc

                if not is_in_range(n_r, n_c):
                    #print("out r c: ", n_r, n_c)
                    break

                #print(str_grids[n_r][n_c], end = " ")
                if str_grids[n_r][n_c] == 'E':
                    e_cnt += 1
                
                n_row = n_r
                n_col = n_c
            
            if e_cnt == 2:
                answer += 1


print(answer)