# cook your dish here
T = int(input())
for i in range(T):
    N,M = input().split()
    N,M = int(N),int(M)
    if N <= M*6*6:
        print("Yes")
    else:
        print("NO")
