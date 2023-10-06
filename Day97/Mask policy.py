for i in range(int(input())):
    N,A = map(int,input().split())
    print(min(A,N-A))
