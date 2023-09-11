for T in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    prod = 1
    for i in range(N):
        prod *=lst[i]
    if prod <0:
        print(1)
    elif prod>0:
        print(0)
    else:
        print(0)
