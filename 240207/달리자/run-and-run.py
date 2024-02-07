n = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

answer = 0

for idx in range(n-1):
    diff = a_arr[idx] - b_arr[idx]
    if diff > 0:
        answer += diff

        a_arr[idx] -= diff
        a_arr[idx+1] += diff

print(answer)