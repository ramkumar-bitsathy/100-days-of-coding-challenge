T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    time = Y//X  
    if Z >time:
        print(Z-time)
    else:
        print(0)
