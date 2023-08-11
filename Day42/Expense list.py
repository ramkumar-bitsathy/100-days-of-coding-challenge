T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    earns = 2**X
    for i in range(N):
        earns = earns-(earns*(50/100))
    print(int(earns))
