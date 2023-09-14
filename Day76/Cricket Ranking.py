for T in range(int(input())):
    R1,W1,C1 = map(int,input().split())
    R2,W2,C2 = map(int,input().split())
    player1 = 0
    player2 = 0
    if R1>R2:
        player1+=1 
    else:
        player2+=1 
    if W1>W2:
        player1+=1 
    else:
        player2+=1 
    if C1>C2:
        player1+=1 
    else:
        player2+=1 
    if player1>player2:
        print("A")
    else:
        print("B")
