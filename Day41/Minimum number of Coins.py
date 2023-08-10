T = int(input())
for i in range(T):
    X = int(input())
    
    if X%10 == 0:
        print(X//10)
    elif X%10==5:
        print((X//10)+1)
    else:
        print(-1)
            
