x, y = map(int, input().split())

def get_sum(n):
    if n < 10:
        return n

    return get_sum(n // 10) + (n%10)

answer = 0

for n in range(x, y+1):
    answer = max(answer, get_sum(n))

print(answer)