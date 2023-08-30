import math
T = int(input())
for i in range(T):
    xa,xb,Xa,Xb = map(int,input().split())
    coc_A = math.ceil(Xa//xa)
    coc_B = math.ceil(Xb//xb)
    print(coc_A+coc_B)
    
