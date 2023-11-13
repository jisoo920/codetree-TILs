MAX = 100
n = int(input())


if n == 1:
    print(0)
    exit()

data_list = [0] *(MAX+1)

for _ in range(n):
    location, alphbet = input().split()
    data_list[int(location)] = alphbet


max_picture = 0


for start in range(MAX):
    g_cnt, h_cnt = 0, 0
    if data_list[start] == 0:
            continue

    if data_list[start] == 'G':
        g_cnt += 1
    elif data_list[start] == 'H':
        h_cnt += 1

    for end in range(start+1, MAX+1):
        #print(start, end)
        #print(data_list[start:end], data_list[end])
        
        if data_list[end] == 0:
            continue

        if data_list[end] == 'G':
            g_cnt += 1
        elif data_list[end] == 'H':
            h_cnt += 1

        #print("g, h: ", g_cnt, h_cnt)
        if g_cnt == h_cnt:
            #print(data_list[start:end+1])
            #print(end-start)
            max_picture = max(max_picture, abs(end-start))


print(max_picture)