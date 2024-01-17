x1, x2, x3, x4 = map(int, input().split())

intersect = True

if x2 < x3 or x4 < x1:
    intersect = False

if intersect:
    print("intersecting")
else:
    print("nonintersecting")