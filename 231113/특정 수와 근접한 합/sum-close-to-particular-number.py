import sys

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

min_gap = sys.maxsize
total_sum = sum(num_list)

for a in range(N):
    for b in range(a, N):
        num_sum = total_sum - (num_list[a] + num_list[b])

        #print(num_list[a], num_list[b], num_sum)

        min_gap = min(min_gap, abs(num_sum - S))

print(min_gap)