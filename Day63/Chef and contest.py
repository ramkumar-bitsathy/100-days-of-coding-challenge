T = int(input())
for i in range(T):
    X,Y,P,Q = map(int,input().split())
    if X+(P*10) > Y+(Q*10):
        print("Chefina")
    elif X+(P*10) < Y+(Q*10):
        print("Chef")
    else:
        print("Draw")
