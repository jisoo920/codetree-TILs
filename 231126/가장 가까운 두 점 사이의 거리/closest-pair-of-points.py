import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize

for i in range(n):
    distance = 0
    for j in range(i+1, n):
        p_1 = points[i]
        p_2 = points[j]

        distance = (p_1[0] - p_2[0]) ** 2 + (p_1[1] - p_2[1]) ** 2

        answer = min(answer, distance)


print(answer)