for T in range(int(input())):
    X1,X2,X3,V1,V2 = map(int,input().split())
    chef1_time = (X3 - X1) / V1
    chef2_time = (X2 - X3) / V2
    if chef1_time > chef2_time :
        print("Kefa")
    elif chef1_time < chef2_time:
        print("Chef")
    else:
        print("Draw")
        

