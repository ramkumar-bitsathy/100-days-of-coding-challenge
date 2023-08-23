T = int(input())
for i in range(T):
    x,y,z = map(int,input().split())
    if (x*y)%z == 0:
        print(x*y,z)
    elif (y*z)%x == 0:
        print(y*z,x)
    elif (z*x)%y == 0:
        print(z*x,y)
    else:
        print(-1)
