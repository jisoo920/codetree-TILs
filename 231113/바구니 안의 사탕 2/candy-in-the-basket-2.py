import sys

MAX =100
n, k = map(int, input().split())

candys = [0]*(MAX+1)

for _ in range(n):
    c, b = map(int, input().split())
    candys[b] += c

#print("candys", candys)

max_cnt = -sys.maxsize

for start in range(MAX):
    #print("center", center)
    sub_can = candys[start:start+2*k+1]
    #print(sub_can)
    cnt = sum(sub_can)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)