n = int(input())
num_ranges = [list(map(int, input().split())) for _ in range(n)]
MAX = 10000

for num in range(1, MAX+1):
    target = num *2
    check = True

    for a, b in num_ranges:
        #print("a, b, target: ", a, b, target)
        if not check:
            continue

        if (target >= a) and (target <= b) :
            check = True
            #print(a, b, target)
            target *= 2
        else:
            check = False
            continue
    
    if check:
        print(num)
        exit()