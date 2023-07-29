import math
T = int(input())
for i in range(T):
    x,y,z = map(int,input().split())
    no_refills = math.ceil(x/y)
    cost = no_refills *z
    print(cost)
