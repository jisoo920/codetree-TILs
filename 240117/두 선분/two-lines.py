x1, x2, x3, x4 = map(int, input().split())

intersect = False

if x1 <= x3 <= x2:
    intersect = True
elif x1 <= x4 <= x2:
    intersect = True
elif x3 <= x1 <= x4:
    intersect = True
elif x3 <= x2 <= x4:
    intersect = True

if intersect:
    print("intersecting")
else:
    print("nonintersecting")