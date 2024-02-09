# 사람 수, 메시지 개수, p번째 메시지
n, m, p = map(int, input().split())
alpha = [chr(c) for c in range(ord('A'),ord('Z')+1)][:n]


reader = list()
for idx in range(1, m+1):
    programer, message = input().split()
    if (idx == p) and message == '0':
        exit()

    if idx >= p:
        reader.append(programer)

unreader = list(set(alpha) - set(reader))

for r in unreader:
    print(r, end = ' ')