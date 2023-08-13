import math
T = int(input())
for i in range(T):
    x,y = 0,0
    x1,y1,x2,y2 = map(int,input().split())
    dis_alex = math.sqrt((x1-x)**2 + (y1-y)**2)
    dis_bob  = math.sqrt((x2-x)**2 + (y2-y)**2)
    if dis_bob>dis_alex:
        print("Bob")
    elif dis_alex>dis_bob:
        print("alex")
    else:
        print("Equal")
