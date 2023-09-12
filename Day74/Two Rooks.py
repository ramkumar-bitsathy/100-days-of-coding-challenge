for T in range(int(input())):
    X1,Y1,X2,Y2 = map(int,input().split())
    if X1==X2 or Y1==Y2:
        print("YES")
    else:
        print("NO")
