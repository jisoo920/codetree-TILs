n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

#print(points)

intersect = True

for idx in range(n-1):
    if points[idx][1] < points[idx][0]:
        intersect = False
    break


if intersect:
    print("Yes")
else:
    print("No")