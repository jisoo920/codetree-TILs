x, y = map(int, input().split())

anwser = 0 

for n in range(x, y+1):
    if str(n) == str(n)[::-1]:
        anwser += 1
print(anwser)