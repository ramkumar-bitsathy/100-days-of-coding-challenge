T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    ages = list(map(int,input().split()))
    count = 0
    for i in ages:
        if i>=X:
            count+=1
    print(f"{count}")
    
