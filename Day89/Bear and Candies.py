for T in range(int(input())):
    A,B = map(int,input().split())
    Limak = 0
    Bob = 0
    winner = None
    choco = 1
    while winner==None:
        if choco%2 !=0:
            Limak +=choco
            if Limak > A:
                winner = "Bob"
                continue
        else:
            Bob+=choco
            if Bob >B:
                winner = "Limak"
                continue
        choco+=1 
        
    print(winner)
        
            
        
