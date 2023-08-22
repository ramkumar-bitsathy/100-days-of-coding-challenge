T = int(input())
for i in range(T):
    x,m,d = map(int,input().split())
    max_time = min(x*m,x+d)
    print(max_time)
