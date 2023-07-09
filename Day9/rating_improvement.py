T = int(input())
for i in range(T):
    X,Y = input().split()
    rating , difficulty = int(X),int(Y)
    if rating <= difficulty <= rating+200:
        print("Yes")
    else:
        print("NO")
