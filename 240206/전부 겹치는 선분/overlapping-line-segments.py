n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

#print(points)

intersect = 0

for idx in range(n-1):
    if points[idx][1] >= points[idx+1][0]:
        intersect += 1


if intersect == n:
    print("Yes")
else:
    print("No")