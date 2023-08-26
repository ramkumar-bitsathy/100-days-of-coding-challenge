T = int(input())
for i in range(T):
    d,x,y,z = map(int,input().split())
    strategy1 = x*7
    strategy2 = (y*d)+((7-d)*z)
    print(max(strategy1,strategy2))
