for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    maxi = A[0]+A[-1]
    for i in range(N-1):
        maxi = max(maxi,A[i]+A[i+1])
    print(maxi)
