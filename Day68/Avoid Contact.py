for T in range(int(input())):
    X,Y = map(int,input().split())
    if X==Y:
        print(X+Y-1)
    else:
        print(X+Y)
