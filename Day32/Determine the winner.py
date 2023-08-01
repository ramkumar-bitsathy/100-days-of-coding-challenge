T = int(input())
for i in range(T):
    Pa,Pb,Qa,Qb = map(int,input().split())
    P = [Pa,Pb]
    Q = [Qa,Qb]
    if max(P)<max(Q):
        print("P")
    elif max(P)>max(Q):
        print("Q")
    else:
        print("TIE")
