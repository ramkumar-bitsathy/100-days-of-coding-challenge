T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    if N//2 < X:
        print(N-X)
    elif N//2 == X:
        print(X)
    elif N//2 > X:
        print(X)
    elif N==X:
        print(0)
