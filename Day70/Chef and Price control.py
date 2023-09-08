for T in range(int(input())):
    N,K = map(int,input().split())
    price = list(map(int,input().split()))
    loss = 0
    for i in range(N):
        if price[i] > K:
            loss += price[i]-K
    print(loss)
