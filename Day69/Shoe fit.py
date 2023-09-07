for T in range(int(input())):
    lst = list(map(int,input().split()))
    if 1 in lst and 0 in lst:
        print(1)
    else:
        print(0)
