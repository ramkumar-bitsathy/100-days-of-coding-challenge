for T in range(int(input())):
    X,A,B=map(int,input().split())
    P=A+(100-X)*B
    print(P*10)
