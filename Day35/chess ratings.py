import math
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    if X == Y:
        print(0)
    elif X<Y:
        rating_diff = Y-X
        print(math.ceil(rating_diff/8))
