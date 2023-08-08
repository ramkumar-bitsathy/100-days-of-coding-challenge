T = int(input())
for i in range(T):
    X1,Y1,X2,Y2 = map(int,input().split())
    distance = max(abs(X1-X2),abs(Y1-Y2))
    print(distance)
