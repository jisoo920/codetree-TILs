n = int(input())
directions = [list(map(int, input().split())) for _ in range(n)]

answer = 0


for s in range(1, 4):    
    stone = [0]*4
    stone[s] = 1
    
    score = 0

    for a, b, c in directions:
        stone[a], stone[b] = stone[b], stone[a]
        
        if stone[c] == 1:
            score += 1
    
    answer = max(answer, score)

print(answer)