import sys

n, h, t = map(int, input().split())
height = list(map(int,input().split()))

cost_h_list = list()
for idx in range(n):
    cost_h_list.append(abs(h-height[idx]))
#print(cost_h_list)

min_cost = sys.maxsize

for start in range(0, n-t+1):
#    print(cost_h_list[start:start+t])
    cost = sum(cost_h_list[start:start+t])
    min_cost = min(min_cost, cost)
    
print(min_cost)