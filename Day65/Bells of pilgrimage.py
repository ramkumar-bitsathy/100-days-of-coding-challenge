for T in range(int(input())):
    N,X,K,P = map(int,input().split())
    mana = 0
    if K <= X:
        mana = P+K*10
    elif K > X:
        mana = P+(X*10)+(K-X)*5
        if K == N:
            mana += 20
    print(mana)
