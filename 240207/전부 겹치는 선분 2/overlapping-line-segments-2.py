n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

#print(points)

# 가장 작은 선분 삭제
a_min_x2 = points[1][1]
a_max_x1 = points[n-1][0]


# 가장 큰 선분 삭제 
b_min_x2 = points[0][1]
b_max_x1 = points[n-2][0]

if a_min_x2 >= a_max_x1 or b_min_x2 >= b_max_x1:
    print("Yes")
else:
    print("No")