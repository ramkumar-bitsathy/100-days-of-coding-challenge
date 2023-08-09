T = int(input())
for i in range(T):
    S,X,Y,Z = map(int,input().split())
    if S-(X+Y) >= Z:
        print(0)
    elif S-(X+Y)+X >= Z or S-(X+Y)+Y >=Z:
        print(1) 
    else:
        print(2)
