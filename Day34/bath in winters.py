import math
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    print(math.floor(X//(Y*2)))
