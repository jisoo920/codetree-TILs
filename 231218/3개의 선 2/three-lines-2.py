n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]

possible = 0

for hor in range(10):
    for ver in range(10):
        checked = [0] * n

        for i in range(len(coord)):
            if coord[i][0] == ver or coord[i][1] == hor :
                checked[i] = 1
            
    
    if sum(checked) == n:
        possible += 1

if possible <= 3:
    print(1)
else:
    print(0)