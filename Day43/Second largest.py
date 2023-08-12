T = int(input())
for i in range(T):
    lst = list(map(int,input().split()))
    des_order = sorted(lst,reverse = True)
    print(des_order[1])
