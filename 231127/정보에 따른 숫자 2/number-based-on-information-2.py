MAX = 1000
t, a, b = map(int, input().split())
points = [0]*(MAX+1)

for _ in range(t):
    alp, x = input().split()
    points[int(x)] = alp

# 가까운 s까지의 거리
def get_d1(p):
    distance = MAX+1
    # 왼쪽
    for i in range(p, 0, -1):
        if points[i] == 'S':
            distance = min(distance, abs(p-i))

    # 오른쪽
    for i in range(p, MAX+1):
        if points[i] == 'S':
            distance = min(distance, abs(p-i))

    return distance

# 가까운 n까지의 거리
def get_d2(p):
    distance = MAX+1
    # 왼쪽
    for i in range(p, 0, -1):
        if points[i] == 'N':
            distance = min(distance, abs(p-i))

    # 오른쪽
    for i in range(p, MAX+1):
        if points[i] == 'N':
            distance = min(distance, abs(p-i))

    return distance
    return 0

answer = 0
for p in range(a, b+1):
    if get_d1(p) <= get_d2(p):
        answer+=1

print(answer)