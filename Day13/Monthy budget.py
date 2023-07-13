T = int(input())
for i in range(T):
    X,Y = input().split()
    rup , exp = int(X),int(Y)
    if exp *30 <= rup:
        print("Yes")
    else:
        print("NO")
