import sys

n, h, t = map(int, input().split())
height_list = list(map(int, input().split()))

min_cost = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cost = abs(h-height_list[i]) + abs(h-height_list[j]) + abs(h-height_list[k])

            min_cost = min(min_cost, cost)

print(min_cost)