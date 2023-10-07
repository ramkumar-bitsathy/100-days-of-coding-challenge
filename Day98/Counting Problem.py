for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    eve_ct = 0
    odd_ct = 0
    for i in range(N):
        if A[i]%2 == 0:
            eve_ct += 1 
        else:
            odd_ct += 1 
            
    if (odd_ct%2 == 0) and (odd_ct> 0):
        print("Yes")
    else:
        print("NO")
            
