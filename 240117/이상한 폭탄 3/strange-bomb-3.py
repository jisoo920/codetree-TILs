n, k = map(int, input().split())
bumbs = [int(input()) for _ in range(n)]
#(폭탄정수, 횟수)
answer = list()

unique_b = list(set(bumbs))

for unique in unique_b:
    idx = 0
    cnt = 0 # 터진 횟수
    for i in range(n):
        if bumbs[i] == unique: 
            if abs(idx-i) <= k:
                cnt += 1
            idx = i

    if cnt > 0:
        answer.append((unique, cnt))

    #print(answer)

if len(answer) == 0:
    print(0)
else:
    answer.sort(key = lambda x:-x[1])
    #print("answer", answer)
    print(answer[0][0])
    # 터진 횟수기준 정렬, 폭탄 번호 출력