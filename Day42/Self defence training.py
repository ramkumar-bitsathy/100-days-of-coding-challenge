T = int(input())
for i in range(T):
    N = int(input())
    lst= list(map(int,input().split()))
    count = 0
    for i in lst:
        if 10<=i<=60:
            count+=1
        
    print(count)
