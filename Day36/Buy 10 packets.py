# cook your dish here
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    if 2*X >= Y:
        print(Y*2+X)
    elif 2*X <Y:
        print(X*5)
