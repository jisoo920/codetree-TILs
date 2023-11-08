import sys

n = int(input())
pepole = [int(input()) for _ in range(n)]

answer = sys.maxsize

for start in range(n):
    idx, distance = 0, 0
    
    for p in range(start, start+n):
        if p >= n:
            p_num = pepole[p-n]
            #print(pepole[p-n], end = " ")
        else:
            p_num = pepole[p]
            #print(pepole[p], end = " ")
        distance += (p_num *idx)
        idx += 1

    answer = min(answer, distance)

print(answer)