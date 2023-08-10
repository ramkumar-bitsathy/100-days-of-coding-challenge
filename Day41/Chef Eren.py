T = int(input())
for i in range(T):
    N,A,B = map(int,input().split())
    tot = 0
    for i in range(1,N+1):
        if i%2==0:
            tot+= A 
        if i%2!=0:
            tot+= B
    print(tot)
