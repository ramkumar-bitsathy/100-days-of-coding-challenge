for T in range(int(input())):
    N = int(input())
    L = list(map(int,input().split()))
    if sum(L)%2 == 1:
        print("YES")
    else:
        print("NO")
