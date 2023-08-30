import math
T = int(input())
for i in range(T):
    M,S = map(int,input().split())
    print(math.floor(M//S))
