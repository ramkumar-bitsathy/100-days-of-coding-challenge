import math
for T in range(int(input())):
    N,M = map(int,input().split())
    tot_area = N*M 
    s= math.gcd(N,M)
    print(int(tot_area/(s*s)))
