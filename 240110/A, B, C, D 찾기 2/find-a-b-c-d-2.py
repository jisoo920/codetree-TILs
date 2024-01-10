nums = sorted(list(map(int, input().split())))

MAX_N = 37
#print(nums)

def is_possible(a, b, c, d):
    num_list = [a, b, c, d]

    num_list.append(a+b)
    num_list.append(b+c)
    num_list.append(c+d)
    num_list.append(d+a)
    num_list.append(a+c)
    num_list.append(b+d)

    num_list.append(a+b+c)
    num_list.append(a+b+d)
    num_list.append(a+c+d)
    num_list.append(b+c+d)

    num_list.append(a+b+c+d)
    #print(a, b, c, d, num_list)
    if sorted(num_list) == nums:
        return True
    else:
        return False



for a in range(min(nums), MAX_N+1):
    for b in range(min(nums), MAX_N+1):
        for c in range(min(nums), MAX_N+1):
            for d in range(min(nums), MAX_N+1):
                if is_possible(a, b, c, d):
                    print(a, b, c, d)
                    exit()