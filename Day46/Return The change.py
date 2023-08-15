T = int(input())
for i in range(T):
    X = int(input())
    rem = X%10
    if rem < 5:
        X=X - rem
    elif rem >= 5:
        X=X+(10-rem)
    print(100-X)
