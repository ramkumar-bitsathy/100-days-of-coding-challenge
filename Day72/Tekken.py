for T in range(int(input())):
    A,B,C = map(int, input().split())
    D = abs(B-C)
    if A > D:
        print("YES")
    else:
        print("NO")
