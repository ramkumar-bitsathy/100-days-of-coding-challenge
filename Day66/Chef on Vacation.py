for T in range(int(input())):
    X,Y,Z = map(int,input().split())
    if X+Y > Z:
        print("NO")
    else:
        print("YES")
