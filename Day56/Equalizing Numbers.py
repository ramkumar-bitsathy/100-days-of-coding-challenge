t=int(input()) 
for i in range(t): 
    a,b=map(int,input().split()) 
    d=abs(a-b) 
    if(d%2==0): 
        print("yes") 
    else: 
        print("no")
