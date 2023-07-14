T = int(input())
for i in range(T):
    X,Y,Z = input().split()
    capacity, no_peoples, cost = int(X),int(Y),int(Z)
    if no_peoples <= capacity*10:
        max_amt = no_peoples * cost
    elif no_peoples > capacity*10:
        max_amt = capacity*10 * cost
    print(max_amt)
