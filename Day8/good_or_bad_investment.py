T  = int(input())
for i in range(T):
    X,Y = input().split()
    interest,inflation = int(X),int(Y)
    if interest >= 2*inflation:
        print("Yes")
    else:
        print("NO")
