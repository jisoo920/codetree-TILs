MAX = 19

girds = [ list(map(int, input().split())) for _ in range(MAX)]

black = [1, 1, 1, 1, 1]
white = [2, 2, 2, 2, 2]

def is_in_range(r, c):
    return 0 <= r <= MAX-1 and 0 <= c <= MAX-1

# 가로
def check_hor(r, c): 
    #print("가로, r, c:", girds[r][c:c+5], r, c)
    
    if girds[r][c:c+5] == black or girds[r][c:c+5] == white:
        return True
    else:
        return False

# 세로
def check_ver(r, c):
    num_list = []
    for n_r in range(r, r+5):
        if not is_in_range(n_r, c):
            return False
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
        if not is_in_range(r+n, c+n):
            return False
        num_list.append(girds[r+n][c+n])

    if num_list == black or num_list == white:
        return True
    else:
        return False


# 역대각선
def check_re_dia(r, c):    
    num_list = []
    for n in range(5):
        if not is_in_range(r+n, c-n):
            return False
        num_list.append(girds[r+n][c-n])
    
    if num_list == black or num_list == white:
        return True
    else:
        return False

how = None
breaker = False
winner = 0
for row in range(MAX):
    if breaker:
        break

    for col in range(MAX):
        n_row, n_col = row, col
        #print("n_row, n_col: ", n_row, n_col)

        
        # 가로
        if n_col <= MAX-5 and check_hor(n_row, n_col):
            how = 'hor'
            breaker = True
            winner = girds[n_row][n_col]
            break
        
        # 세로
        if n_row <= MAX-5 and check_ver(n_row, n_col):
            how = 'ver'
            breaker = True
            winner = girds[n_row][n_col]
            break
        
        # 대각선
        if n_row <= MAX-5 and n_col <= MAX-5 and check_dia(n_row, n_col):
            how = 'dia'
            breaker = True
            winner = girds[n_row][n_col]
            break
        
        # 역대각선
        if n_col >= 5 and n_row <= MAX-5 and check_re_dia(n_row, n_col):
            how = 're_dia'
            breaker = True
            winner = girds[n_row][n_col]
            break
        
        #break
        
        
        
        


#print("n_row, n_col, how:", n_row, n_col, how)

# 이긴 돌
print(winner)

if winner != 0:
    # 가로
    if how == 'hor':     
        print(n_row+1, n_col+3)
    # 세로
    elif how == 'ver' :
        print(n_row+3, n_col+1)
    # 대각선
    elif how == 'dia' :
        print(n_row+3, n_col+3)
    # 역대각선
    elif how == 're_dia':
        print(n_row+3, n_col-1)