T = int(input())
for i in range(T):
    X,Y = input().split()
    double , triple = int(X),int(Y)
    cost1 = double * 3
    cost2 = triple * 2 
    if cost1 < cost2:
        print(cost1)
    else:
        print(cost2)
