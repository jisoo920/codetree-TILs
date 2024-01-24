import sys

n = int(input())
heights = [int(input()) for _ in range(n)]

MAX_NUM = 17
MAX_H = 100
cost = sys.maxsize

for i in range(MAX_H):
    # i부터 i+MAX_NUM까지 값이 들어오게 조정 후 cost 계산
    now_cost = 0

    for j in range(n):
        if i <= heights[j] <= (i+MAX_NUM):
            continue
        elif heights[j] < i : # 3 5 +2
            now_cost += (heights[j] - i)**2
        elif heights[j] > (i+MAX_NUM): # 30 22 -8
            now_cost += (heights[j] - (i+MAX_NUM))**2

    cost = min(cost, now_cost)

print(cost)