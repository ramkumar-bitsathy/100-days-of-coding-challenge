for T in range(int(input())):
    Amin,Bmin,Cmin,Tmin,A,B,C = map(int,input().split())
    if A >= Amin and B >= Bmin and C >= Cmin:
        if A+B+C >= Tmin:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
