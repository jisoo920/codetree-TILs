import sys

developers = list(map(int, input().split()))

sum_de = sum(developers)
def get_diff(i, j, k):
    sum_1= developers[i] + developers[j] + developers[k]
    sum_2 = sum_de - sum_1
    return abs(sum_1-sum_2)




len_de = len(developers)


answer = sys.maxsize

for i in range(len_de):
    for j in range(i+1, len_de):
        for k in range(j+1, len_de):
            answer = min(answer, get_diff(i, j, k))

print(answer)