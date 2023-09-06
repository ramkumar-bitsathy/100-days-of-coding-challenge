for T in range(int(input())):
    N,M = map(int,input().split())
    if abs(N-M)%2 == 0:
        print("YES")
    else:
        print("NO")
        
