for T in range(int(input())):
    N = int(input())
    run_lst = list(map(int,input().split()))
    runs = 0
    count = 0
    for i in range(N):
        runs += run_lst[i]
        if (runs/(i+1)) == 1:
            count +=1
    print(count)
        
