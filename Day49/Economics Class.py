T = int(input())
for i in range(T):
    N = int(input())
    S = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    count = 0
    for j in range(N):
        if S[j] == D[j]:
            count+= 1  
    print(count)
        
