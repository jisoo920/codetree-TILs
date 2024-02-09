# 사람 수, 메시지 개수, p번째 메시지
n, m, p = map(int, input().split())
alpha = [chr(c) for c in range(ord('A'),ord('Z')+1)][:n]
messages = [list(input().split()) for _ in range(m)]

reader = list()

# p번째 메시지를 모두가 읽었을 때
if messages[p-1][1] == '0':
    exit()

# p번째와 그 이후의 사람은 읽음
for programer, msg in messages[p-1:]:
    reader.append(programer)

# p번째보다 앞선 메시지 중에, 읽은 수가 같으면 같이 읽음
for idx in range(p-2, -1, -1):
    #print("messages[idx]: ", messages[idx])
    if messages[idx][1] == messages[p-1][1]:
        reader.append(messages[idx][0])

#print("reader: ", reader)
unreader = list(set(alpha) - set(reader))

for r in unreader:
    print(r, end = ' ')