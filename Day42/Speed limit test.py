T = int(input())
for i in range(T):
    A,X,B,Y = map(int,input().split())
    alice = A/X 
    bob = B/Y
    if alice > bob:
        print("alice")
    elif alice<bob:
        print("bob")
    else:
        print("Equal")
