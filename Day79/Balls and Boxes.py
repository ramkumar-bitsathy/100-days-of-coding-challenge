for T in range(int(input())):
    N,K = map(int,input().split())
    balls = (K*(K+1))//2
    if N>=balls:
        print("Yes")
    else:
        print("NO")
