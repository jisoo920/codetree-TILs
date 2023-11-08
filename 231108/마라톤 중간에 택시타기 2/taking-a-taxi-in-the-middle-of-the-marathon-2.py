import sys

n = int(input())
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append([x, y])

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

answer = sys.maxsize

for idx in range(n):
    left = 0
    right = 1

    if idx == 0 or idx == n-1:
        continue

    distance = 0
    for j in range(1, n):
        if j == idx: 
            right = j + 1

        if right >= n:
            continue
        #print("left, right: ", left, right)
        distance += get_distance(coord[left][0], coord[left][1], coord[right][0], coord[right][1])

        left = right
        right += 1

    answer = min(distance, answer)

print(answer)