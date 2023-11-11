import sys

n = int(input())
num_list = [int(input()) for _ in range(n)]

def is_carry(a, b, c):
    return True if sum([a, b, c]) >= 10 else False

def check_and_sum(a, b, c):
    real_a, real_b, real_c = a, b, c
    #print("a, b, c: ", real_a, real_b, real_c)

    while True:
        check_a, check_b, check_c = a%10, b%10, c%10,
        #print("F", check_a, check_b, check_c)          

        if is_carry(check_a, check_b, check_c): # carry 발생, 종료
            return -1
        
        a = (a-check_a)//10
        b = (b-check_b)//10
        c = (c-check_c)//10

        if a == 0 and b == 0 and c == 0:
            #print(f'{check_a} + {check_b} +{check_c} = {check_a + check_b + check_c}')
            return real_a + real_b + real_c  

        #print("S", a, b, c)


answer = -sys.maxsize
for i in range(n-2):
    for j in range(+1, n-1):
        for k in range(j+1, n):
            #print(i, j, k)
            #rint("Wow", num_list[i], num_list[j], num_list[k])
            #num_sum = check_and_sum(num_list[i], num_list[j], num_list[k])
            answer = max(answer, check_and_sum(num_list[i], num_list[j], num_list[k]))
            
print(answer)