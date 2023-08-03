T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    
    if X<Y:
        print(Y-X)
    elif X>Y:
        print(X-Y)
    else:
        print(0)
