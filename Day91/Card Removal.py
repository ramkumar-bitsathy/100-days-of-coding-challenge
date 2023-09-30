for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    max_count = 0
    for i in range(N):
        if A.count(A[i]) >max_count:
            max_count = A.count(A[i])
    print(N - max_count)
        
