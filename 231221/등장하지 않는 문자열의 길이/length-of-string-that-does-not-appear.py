n = int(input())
string = input()

answer = 100

for l in range(1, n+1):
    count = 1
    sub_string = string[:l]
    #print(sub_string)
    for start in range(1, n):
        if string[start:start+l] == sub_string:
            count += 1

    #print(l, count)
    if count == 1:
        answer = min(answer, l)

print(answer)