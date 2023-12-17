n = int(input())
numbers = list(map(int, input().split()))

answer = 9999

for double in range(n):
    numbers[double] = int(numbers[double]*2)
    
    for rm in range(n):
        rm_numbers = [numbers[i] for i in range(n) if i != rm ]
        
        score = 0
        
        for i in range(len(rm_numbers)-1):
            score += abs(rm_numbers[i] - rm_numbers[i+1])

        answer = min(score, answer)
    
    numbers[double] = int(numbers[double]/2)
    
print(answer)