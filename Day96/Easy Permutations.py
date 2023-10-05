for T in range(int(input())):
    N = int(input())
    lst = list()
    for i in range(1,N+1):
        lst.append(i)
    print(*lst[::-1])
