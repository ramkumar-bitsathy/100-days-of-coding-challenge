T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    to_be_drawn = 21-(A+B)
    
    if to_be_drawn>10:
        print(-1)
    else:
        print(to_be_drawn) 
