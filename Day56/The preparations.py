T = int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    if N*K < M:
        print("Yes")
    else:
        print("NO")
