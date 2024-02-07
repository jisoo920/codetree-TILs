n = int(input())

birds = [-1] * (10+1)
answer = 0
for idx in range(n):
    bird_n, location = map(int, input().split())

    # 첫방문
    if birds[bird_n] == -1:
        birds[bird_n] = location
    
    # 두번째 이상 방문 & 이동 X
    elif birds[bird_n] == location:
        continue

    # 두번째 이상 방문 & 이동 O
    elif birds[bird_n] != location:
        answer += 1
        birds[bird_n] = location

    else:
        print("예외")
        print(bird_n, location)

print(answer)