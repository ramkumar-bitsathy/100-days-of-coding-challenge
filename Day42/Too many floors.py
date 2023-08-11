T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    chef_floor = (X-1)//10 +1
    chefina_floor = (Y-1)//10 +1
    diff = abs(chefina_floor-chef_floor)
    print(diff)
