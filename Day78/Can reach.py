for T in range(int(input())):
    x,y,K = map(int,input().split())
    if abs(x)%K == 0 and abs(y)%K == 0:
        print("YES")
    else:
        print("NO")
