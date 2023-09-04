for T in range(int(input())):
    G1,S1,B1,G2,S2,B2 = map(int,input().split())
    if G1+S1+B1 > G2+S2+B2:
        print(1)
    elif G1+S1+B1 < G2+S2+B2:
        print(2)
    
