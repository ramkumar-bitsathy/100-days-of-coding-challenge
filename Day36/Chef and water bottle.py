import math
T = int(input())
for i in range(T):
    N,X,K = map(int,input().split())
    needed_litres = X 
    can_fill = K//needed_litres
    if can_fill>=N:
        print(N)
    else:
        print(can_fill)
