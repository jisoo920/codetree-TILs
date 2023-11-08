n = int(input())
combi = list(map(int, input().split()))

def is_in_range(origin, num):
    if abs(origin-num) <= 2:
        return True
    else:
        return False

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if is_in_range(combi[0], i) or is_in_range(combi[1], j) or is_in_range(combi[2], k):
                #print(i, j, k)
                cnt += 1

print(cnt)