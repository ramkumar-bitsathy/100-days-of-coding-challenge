import math
T = int(input())
for i in range(T):
    N,K,M = map(int,input().split())
    capacity = K*M 
    no_of_bags = math.ceil(N/capacity)
    print(no_of_bags)
