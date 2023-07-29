T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    if Z%X == 0 and Z%Y!=0:
        print("Chicken")
    elif Z%X != 0 and Z%Y == 0:
        print("Duck")
    elif Z%X ==0 and Z%Y == 0:
        print("Any")
    elif Z%X!=0 and Z%Y !=0:
        print("None")
        
