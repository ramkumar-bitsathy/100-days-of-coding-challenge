import math
T = int(input())
for i in range(T):
    
    N,X = map(int,input().split())
    if N>X:
        candies = math.ceil((N-X)/4)  
        print(candies)
    else:
        print(0)
