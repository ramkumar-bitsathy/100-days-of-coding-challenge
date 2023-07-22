
import math
T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    tot_pieces = N*X 
    min_pizzas = math.ceil(tot_pieces/4)
    print(min_pizzas)
    
