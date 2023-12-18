import sys

MAX = 100

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

anwser = sys.maxsize

for ver in range(2, MAX+1, 2):
    for hor in range(2, MAX+1, 2):
        section_1, section_2, section_3, section_4 = 0, 0, 0, 0

        for x, y in points:
            if x < hor and y < ver:
                section_1 += 1

            if x > hor and y < ver:
                section_2 += 1
            
            if x < hor and y > ver:
                section_3 += 1
            
            if x > hor and y > ver:
                section_4 += 1
        
        this_m = max(max(section_1, section_2), max(section_3, section_4))

        anwser = min(this_m, anwser)

print(anwser)