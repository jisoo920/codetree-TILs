x, y = map(int, input().split())

answer = 0

for n in range(x, y+1):
    str_n = str(n)
    #print(str_n)
    sum_num = 0
    for s_n in str_n:
        sum_num += int(s_n)
    
    answer = max(answer, sum_num)

print(answer)