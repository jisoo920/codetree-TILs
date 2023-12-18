a, b, c = map(int, input().split())

answer = 0

a_max = c // a
b_max = c //b

for i in range(a_max+1):
    for j in range(b_max+1):
        value = (a*i) + (b*j)
        if value <= c :
            answer = max(answer, value)

print(answer)