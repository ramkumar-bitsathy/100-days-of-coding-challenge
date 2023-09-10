for T in range(int(input())):
    P,M,V = map(int,input().split())
    P-=1
    print((M-P)*V)
