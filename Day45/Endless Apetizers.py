import math
T = int(input())
for i in range(T):
    X,Y,R = map(int,input().split())
    total_sticks_eaten = X+(R//30)
    plates = math.ceil(total_sticks_eaten/Y)
    print(plates)
