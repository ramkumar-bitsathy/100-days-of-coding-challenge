for T in range(int(input())):
    X,Y,Z = map(int,input().split())
    if X*Y <= X*Z:
        print((X*Z)-(Y*X))
        
