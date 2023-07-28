T = int(input())
for i in range(T):
    N = int(input())
    to_do = list(map(int,input().split()))
    count = 0
    for i in to_do:
        if i>=1000:
            count += 1
    print(count)
        
