T = int(input())
for i in range(T):
    N,X,Y,A,B = map(int,input().split())
    cost_petrol = (N/A)*X 
    cost_diesel = (N/B)*Y  
    if cost_petrol<cost_diesel:
        print("Petrol")
    elif cost_diesel<cost_petrol:
        print("Diesel")
    else:
        print("Any")
