for T in range(int(input())):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if lst[i]>K:
            #lst.remove(lst[i])
            count +=1
    print(count)
