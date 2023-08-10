T = int(input())
for i in range(T):
    X,Y,D = map(int,input().split())
    if abs(X-Y) <=D:
        print("YES")
    else:
        print("NO")
