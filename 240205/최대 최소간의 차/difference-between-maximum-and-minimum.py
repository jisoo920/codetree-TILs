import sys

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

answer = sys.maxsize

MAX = max(numbers)
MIN = min(numbers)

def get_cost(min_num, max_num):
    cost = 0
    for num in numbers:
        # 범위안에 들어오면 pass
        if num >= min_num and num <= max_num: 
            continue
        # 최소값보다 작으면 최소값으로
        elif num < min_num:
            cost += abs(num - min_num)
        # 최대값보다 크면 최대값으로
        elif num > max_num:
            cost += abs(num - max_num)
        
    return cost
    
        
for i in range(MIN, MAX+1):
    max_num = i+k
    answer = min(answer, get_cost(i, max_num))


print(answer)