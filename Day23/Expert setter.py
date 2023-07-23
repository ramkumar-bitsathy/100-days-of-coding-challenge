T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    if Y>= (X*1/2):
        print("YES")
    else:
        print("no")
