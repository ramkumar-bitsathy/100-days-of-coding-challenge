import math
for T in range(int(input())):
    N,K = map(int,input().split())
    print(math.ceil(N/5)-math.ceil(K/5))
