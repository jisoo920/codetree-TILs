MAX = 19

girds = [ list(map(int, input().split())) for _ in range(MAX)]

black = [1, 1, 1, 1, 1]
white = [2, 2, 2, 2, 2]


# 가로
def check_hor(r, c): 
    #print("가로:", girds[r][c:c+5])
    
    if girds[r][c:c+5] == black or girds[r][c:c+5] == white:
        return True
    else:
        return False

# 세로
def check_ver(r, c):
    num_list = []
    for n_r in range(r, r+5):
        num_list.append(girds[n_r][c])
    
    #print(num_list)
    
    if num_list == black or num_list == white:
        return True
    else:
        return False


# 대각선
def check_dia(r, c):    
    num_list = []
    for n in range(5):
        num_list.append(girds[r+n][c+n])

    if num_list == black or num_list == white:
        return True
    else:
        return False

breaker = False
for row in range(MAX-4):
    if breaker:
        break

    for col in range(MAX-4):
        n_row, n_col = row, col
        #print("n_row, n_col: ", n_row, n_col)

        
        # 가로
        if check_hor(n_row, n_col):
            how = 'hor'
            breaker = True
            break
        
        # 세로
        if check_ver(n_row, n_col):
            how = 'ver'
            breaker = True
            break
        
        # 대각선
        if check_dia(n_row, n_col):
            how = 'dia'
            breaker = True
            break
        
        #break
        
        

#print("n_row, n_col, how:", n_row, n_col, how)

# 이긴 돌
print(girds[n_row][n_col])

if girds[n_row][n_col] != 0:
    # 가로
    if how == 'hor':     
        print(n_row+1, n_col+3)
    # 세로
    elif how == 'ver' :
        print(n_row+3, n_col+1)
    # 대각선
    elif how == 'dia' :
        print(n_row+3, n_col+3)