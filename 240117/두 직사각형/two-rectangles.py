x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

intersect = True

if x2 < a1 and y2 < b1:
    intersect = False
elif a2 < x1 and b2 < y2:
    intersect = False
elif b2 < y1 and a2 < y1:
    intersect = False
elif y2 < b1 and x2 < b1:
    intersect = False

if intersect:
    print("overlapping")
else:
    print("nonoverlapping")