T = int(input())
for i in range(T):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=a*b-sum(c)
    if d>0:
        print(d)
    else:
        print(0)
    
