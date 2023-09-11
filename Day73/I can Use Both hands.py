import math
for T in range(int(input())):
    L,R,M = map(int,input().split())
    print(math.ceil(M/L)+math.floor(M/R))
