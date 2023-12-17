n = int(input())
directions = [list(map(int, input().split())) for _ in range(n)]

answer = 0


for s in range(3):    
    stone = [0, 0, 0]
    stone[s] = 1
    
    score = 0

    for d in directions:
        a = d[0]-1
        b = d[1]-1
        c = d[2]-1

        tmp = stone[a]
        stone[a] = stone[b]
        stone[b] = tmp

        if stone[c] == 1:
            score += 1
    
    answer = max(answer, score)

print(answer)