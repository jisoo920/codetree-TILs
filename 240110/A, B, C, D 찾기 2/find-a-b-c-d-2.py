nums = sorted(list(map(int, input().split())))

MAX_N = 37

def is_possible(a, b, c, d):
    num_list = [a, b, c, d]

    num_list.extend([a+b, b+c, c+d, d+a, a+c, b+d])
    num_list.extend([a+b+c, a+b+d, a+c+d, b+c+d])
    num_list.append(a+b+c+d)

    if sorted(num_list) == nums:
        return True
    else:
        return False


for a in range(min(nums), MAX_N+1):
    for b in range(a, MAX_N+1):
        for c in range(b, MAX_N+1):
            for d in range(c, MAX_N+1):
                if is_possible(a, b, c, d):
                    print(a, b, c, d)
                    exit()