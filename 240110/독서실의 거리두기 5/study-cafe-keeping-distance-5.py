n = int(input())
seats = list(input())

def get_distance():
    dist = 100

    for i in range(n):
        for j in range(i+1, n):
            if seats[i] == '1' and seats[j] == '1':
                dist = min(dist, j-i)

    return dist


answer = 0

for i in range(n):
    if seats[i] == '0':
        seats[i] = '1'
        
        answer = max(answer, get_distance())

        seats[i] = '0'
    

print(answer)