for T in range(int(input())):
    X,H = map(int,input().split())
    count = 0
    while H>0:
        if count<5:
            H-=X//2
        else:
            H-=X 
        count +=1 
    print(count)
        
