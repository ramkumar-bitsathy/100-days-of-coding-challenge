T = int(input())
for i in range(T):
    X,Y,Z = input().split()
    rent, purchase, mon = int(X),int(Y),int(Z)
    if mon*rent < purchase:
        print("Yes")
    else: 
        print("NO")
