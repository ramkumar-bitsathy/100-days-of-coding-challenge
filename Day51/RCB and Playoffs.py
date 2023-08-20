T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    if X+Z*2 >= Y:
        print("YES")
    else:
        print("NO")
