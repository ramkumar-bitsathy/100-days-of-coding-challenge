T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    if A*10 > B*5:
        print("First")
    elif A*10 < B*5:
        print("Second")
    else:
        print("Any")
    
