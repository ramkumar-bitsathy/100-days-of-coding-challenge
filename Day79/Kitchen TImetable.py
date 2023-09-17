for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    rem = A[0]
    count = 0
    for i in range(0,N):
        if i > 0:
            rem = A[i]-A[i-1]
        if B[i]<=rem:
            count+=1
    print(count)
            
            
        
