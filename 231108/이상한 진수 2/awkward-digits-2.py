import sys

a =  list(map(int, input()))

answer = -sys.maxsize

for idx in range(len(a)):
    # 1 > 0, 0 >1
    a[idx] = 1 - a[idx] 
    
    num = 0
    for j in range(len(a)):
        num = num*2 + a[j]

    answer = max(answer, num)

    # 1 > 0, 0 >1
    a[idx] = 1 - a[idx] 
    
print(answer)