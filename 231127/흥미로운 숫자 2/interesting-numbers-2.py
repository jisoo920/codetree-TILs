x, y = map(int, input().split())

answer = 0

for num in range(x, y+1):
    cnt_list = [0]*10
    num_list = list()
    for s in str(num):
        cnt_list[int(s)] += 1
        num_list.append(int(s))
    num_set = set(num_list)
    num_tuple = tuple(num_set)
    if len(num_set) == 2:
        if cnt_list[num_tuple[0]] == 1 or cnt_list[num_tuple[1]] == 1:
            answer += 1
    else:
        continue

print(answer)