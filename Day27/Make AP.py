T = int(input())
for i in range(T):
    A,C = map(int,input().split())
    B = (A+C)/2
    if (B % 1)==0:
        print(int(B))
    else:
        print(-1)
