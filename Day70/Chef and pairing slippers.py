for T in range(int(input())):
    N,L,X = map(int,input().split())
    print(min(L,N-L)*X)
