T = int(input())
for i in range(T):
    X,Y,Z= map(int,input().split())
    if Y%Z==0:
        print((Y//Z)*X)
    else:
        print((Y//Z+1)*X)

    
    
        
