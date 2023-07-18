import math
T = int(input())
for i in range(T):
    N,X = input().split()
    N,X = int(N),int(X)
    no_of_sub = math.ceil(N/6)
    print(no_of_sub*X)
    
