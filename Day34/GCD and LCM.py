import math
def lcm(x,y):
    return math.lcm(x,y)
def gcd(x,y):
    return math.gcd(x,y)
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(gcd(A,B),lcm(A,B))
