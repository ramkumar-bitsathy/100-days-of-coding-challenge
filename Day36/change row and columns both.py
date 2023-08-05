T = int(input())
for i in range(T):
    sx,sy,ex,ey = map(int,input().split())
    if sx == ex or sy == ey:
        print(2)
    else:
        print(1)
