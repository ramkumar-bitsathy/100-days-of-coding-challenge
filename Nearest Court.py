T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    mid = (X+Y)//2
    chef = abs(X-mid)
    chefina = abs(Y-mid)
    print(max(chef,chefina))
