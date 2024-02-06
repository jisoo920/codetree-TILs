n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

min_x2 = points[0][1]
max_x1 = points[n-1][0]

if min_x2 >= max_x1:
    print("Yes")
else:
    print("No")