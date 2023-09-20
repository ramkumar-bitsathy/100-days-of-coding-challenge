for T in range(int(input())):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    out = ''
    
    for i in range(N):
        if A[i] <= K:
            out +='1'
            K-=A[i]
        else:
            out+='0'
        
    print(out)
