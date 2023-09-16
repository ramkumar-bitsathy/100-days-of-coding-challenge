for T in range(int(input())):
    A,B,C,D = map(int,input().split())
    if A<B:
        A+=C
        if A<B:
            A+=D 
        else:
            B+=D 
    else:
        B+=C
        if A<B:
            A+=D 
        else:
            B+=D 
    
    if A<B:
        print("S")
    else:
        print("N")
