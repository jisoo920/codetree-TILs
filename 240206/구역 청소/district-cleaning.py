a, b = map(int, input().split())
c, d = map(int, input().split())

# 겹치지 않는 경우 
if b <= c or d <= a:
    answer = (b-a) + (d-c)

# 일부가 겹치는 경우
elif c < b < d or a < d < b:
    answer = max(b, d) - min(a, c)

# 포함되어 겹치는 경우
elif c <= a and b <= d:
    answer = d - c
elif a <= c and d <= b:
    answer = b - a


print(answer)