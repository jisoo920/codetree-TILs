import sys

n = int(input())

x_dots = list()
y_dots = list()

for idx in range(n):
    x, y = map(int, input().split())
    x_dots.append(x)
    y_dots.append(y)

answer = sys.maxsize

for i in range(n):
    area = 0

    for j in range(n):
        #print("del: ", x_dots[i], y_dots[i])
        new_xs = x_dots[:i] + x_dots[i+1:]
        width = max(new_xs) - min(new_xs)
        
        new_ys = y_dots[:i] + y_dots[i+1:]
        height = max(new_ys) - min(new_ys)
        
        area = width * height

        answer = min(area, answer)

print(answer)