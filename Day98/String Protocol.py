for T in range(int(input())):
    N = int(input())
    S = input()
    n = N
    c = 0
    while(c<(len(S)-1)):
        if(S[c]==S[c+1]):
            c+=2
            n-=1
        else:
            c+=1
    print(n)
