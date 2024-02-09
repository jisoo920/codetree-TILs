x = int(input())

speed, second, distance = 1, 1, 1
# 1 증가 0 유지 -1 감소 
how = 1

while True:
    #print("speed, distance, how", speed, distance, how)
    if distance >= x :
        break

    # 증가 조건 체크 

    # 아직 증가조건일 때, 계속 증가인지 확인 
    if how > 0: 
        now_distance = distance + (speed+1)
        #print("now_distance: ", now_distance)
        if (x-now_distance) < distance:
            how = 0
    
    # 유지조건일 때, 계속 유지인지 확인 
    if how <= 0:
        now_distance = distance + speed
        th = sum(i for i in range(1, speed))
        #print("now_distance, th: ", now_distance, th)
        if (x-now_distance) < th:
            how = -1
        else:
            how = 0

        
    # 증가
    if how > 0:
        speed += 1
        distance = now_distance
    # 유지
    elif how == 0:
        distance += speed
    # 감소 
    else:
        speed -= 1
        if speed < 1:
            speed = 1

        distance += speed

    second += 1


print(second)