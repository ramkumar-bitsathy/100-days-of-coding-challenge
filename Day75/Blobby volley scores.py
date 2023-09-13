for T in range(int(input())):
    n=int(input())
    s=input()
    server=0
    alice=0
    bob=0
    for i in range(n):
        if((server==0)and(s[i]=='A')):
            alice+=1
        elif((server==0)and(s[i]=='B')):
            server=1
        elif((server==1)and(s[i]=='B')):
            bob+=1
        else:
            server=0
    print(alice,'',bob)
        
        
            
