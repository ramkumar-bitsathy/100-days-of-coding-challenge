T = int(input())
for i in range(T):
    X,Y = input().split()
    X,Y = int(X),int(Y)
    if Y<= (107/100)*X:
        print("Yes")
    else:
        print("No")
