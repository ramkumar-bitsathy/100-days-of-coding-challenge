T = int(input())
for i in range(T):
    X,Y = input().split()
    X,Y = int(X),int(Y)
    if X*15 >= 2*Y:
        print("Yes")
    else:
        print("No")
