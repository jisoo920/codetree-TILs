n = int(input())

heights = [int(input()) for _ in range(n)]

max_count = 0

for water in range(1, max(heights)+1):
    count = 0
    flag = False
    for h in heights:
        if h > water:
            if flag:
                continue
            else:
                flag = True
                count += 1
        elif h <= water:
            flag = False


    max_count = max(max_count, count)

print(max_count)