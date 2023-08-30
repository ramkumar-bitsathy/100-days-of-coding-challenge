T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    if X+Y >Z:
        print("TRAIN")
    elif X+Y < Z:
        print("PLANEBUS")
    else:
        print("EQUAL")
