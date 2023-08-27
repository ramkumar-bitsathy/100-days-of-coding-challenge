import math
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    print(round(math.sqrt(2*(X-Y))))
