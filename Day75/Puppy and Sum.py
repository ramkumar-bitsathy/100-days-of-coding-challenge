for T in range(int(input())):
    D,N = map(int,input().split())
    res = 0
    for i in range(D):
        res = N*(N+1)//2
        N=res
    print(res)
