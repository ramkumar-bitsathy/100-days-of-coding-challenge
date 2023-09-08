for T in range(int(input())):
    X,Y = map(int,input().split())
    if ((X**4)+4*(Y**2)) == 4*(X**2)*Y:
        print("YES")
    else:
        print("NO")
