n, c, g, h = map(int, input().split())

Tas = list()
Tbs = list()

for _ in range(n):
    ta, tb = map(int, input().split())
    Tas.append(ta)
    Tbs.append(tb)

answer = 0

for temp in range(min(Tas), max(Tbs)+1):
    working = 0
    #print("온도", temp)
    for ta, tb in zip(Tas, Tbs):
        #print("ta, tb", ta, tb)
        if temp < ta:
            working += c
        elif ta <= temp <= tb:
            working += g
        elif temp > tb:
            working += h
        #print("working", working)
    answer = max(answer, working)

print(answer)