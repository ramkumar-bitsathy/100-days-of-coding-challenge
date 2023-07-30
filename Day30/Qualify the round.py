T= int(input())
for i in range(T):
    X,A,B = map(int,input().split())
    scored = A*1 + B*2
    if scored>=X:
        print("Qualify")
    else:
        print("Notqualify")
