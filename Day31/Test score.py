T = int(input())
for i in range(T):
    N,X,Y = map(int,input().split())
    if Y == 0:
        print("yes")
    elif N*X == Y:
        print("YES")
    elif Y%X == 0:
        print("Yes")
    else:
        print("NO")
