T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    freshness = list(map(int,input().split()))
    costofeach = list(map(int,input().split()))
    total_cost = 0
    for i in range(N):
        if freshness[i] >=X:
            total_cost+=costofeach[i]
        
    print(total_cost)
