T = int(input())
for i in range(T):
    W,X,Y,Z = input().split()
    bal , sal, ded, mon = int(W),int(X),int(Y),int(Z)
    for i in range(mon):
        bal = bal+ sal-ded
    
    print(bal)
