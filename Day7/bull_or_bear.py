T = int(input())
for i in range(T):
    X,Y = input().split()
    bought,sold = int(X),int(Y)
    rem = sold-bought
    if rem>0:
        print("PROFIT")
    elif rem<0:
        print("LOSS")
    else:
        print("NEUTRAL")
