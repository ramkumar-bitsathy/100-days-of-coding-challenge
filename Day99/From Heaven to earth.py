import math
for T in range(int(input())):
    N,V1,V2 = map(int,input().split())
    stair_time = (V1* math.sqrt(2))/N
    eleva_time = (V2)/N
    if stair_time > eleva_time:
        print("Stairs")
    else:
        print("Elevator")
