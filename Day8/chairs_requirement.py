
T = int(input())
for i in range(T):
    X,Y = input().split()
    stud,chairs = int(X),int(Y)
    if stud > chairs:
        print(stud - chairs)
    elif stud<= chairs:
        print(0)
