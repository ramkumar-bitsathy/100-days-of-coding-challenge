for T in range(int(input())):
    D,d,A,B,C = map(int,input().split())
    if (D*d) <10:
        print(0)
    elif 10<= (D*d)<21:
        print(A)
    elif 21<=(D*d)<42:
        print(B)
    else:
        print(C)
        
