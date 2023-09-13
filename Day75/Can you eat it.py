for i in range(int(input())):
    N,K = map(int,input().split())
    if N%K == 0:
        print(N//K)
    else:
        print(-1)
