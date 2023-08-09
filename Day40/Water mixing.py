T = int(input())
for i in range(T):
    A,B,X,Y = map(int,input().split())
    if B>A:
        for i in range(0,X):
            A+=1 
            if A ==B:
                print("Yes")
                break
        else:
            print("No")
    elif B<A:
        for i in range(0,Y):
            A-=1 
            if A==B:
                print("Yes")
                break
        else:
            print("NO")
    elif A==B:
        print("Yes")
            
        
