for T in range(int(input())):
    x,y,xr,yr,D = map(int,input().split())
    if (xr*D) <= x and (yr*D) <= y:
        print("YES")
    else:
        print("NO")
