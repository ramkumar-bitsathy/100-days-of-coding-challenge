for i in range(int(input())):
    X,A,B,C=map(int,input().split())
    m=min(A,B,C)
    mx=max(A,B,C)
    print((X-1)*m+(A+B+C-m-mx))
