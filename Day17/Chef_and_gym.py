T = int(input())
for i in range(T):
    X,Y,Z = input().split()
    X,Y,Z = int(X),int(Y),int(Z)
    if  X<=Z<X+Y:
        print(1)
    elif Z<X:
        print(0)
    elif Z>= X+Y:
        print(2)
        
