T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    each_gets = 0
    if N%M == 0:
        each_gets += N//M 
        if each_gets %2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        
        
    
