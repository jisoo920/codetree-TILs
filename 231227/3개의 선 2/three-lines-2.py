MAX_C = 10

n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]

possible = 0

for i in range(MAX_C+1):
    for j in range(MAX_C+1):
        for k in range(MAX_C+1):
            
            # ver 3 hor 0
            checked = True
            for x, y in coord:
                if y == i or y == j or y == k:
                    continue            
                checked = False
            
            if checked: 
                possible = 1


            # ver 2 hor 1
            checked = True
            for x, y in coord:
                if y == i or y == j or x == k:
                    continue            
                checked = False
            
            if checked: 
                possible = 1

            # ver 1 hor 2
            checked = True
            for x, y in coord:
                if y == i or x == j or x == k:
                    continue            
                checked = False
            
            if checked: 
                possible = 1

            # ver 0 hor 3
            checked = True
            for x, y in coord:
                if x == i or x == j or x == k:
                    continue            
                checked = False
            
            if checked: 
                possible = 1


print(possible)