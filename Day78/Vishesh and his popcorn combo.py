for T in range(int(input())):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    print(max(sum(A),sum(B),sum(C)))
