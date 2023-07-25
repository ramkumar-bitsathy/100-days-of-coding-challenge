T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    alice = 400/X
    bob = 400/Y
    charlie = 400/Z
    if alice>bob and alice > charlie:
        print("Alice")
    elif bob>alice and bob>charlie:
        print("Bob")
    else:
        print("charlie")
