for T in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    max_count = 0
    for i in lst:
        if lst.count(i) >max_count:
            max_count = lst.count(i)
    print(N- max_count)
