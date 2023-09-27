for T in range(int(input())):
    N = int(input())
    S = input()
    enc1 = ''
    enc2 = ''
    if N%2!=0:
        for i in range(0,N-2,2):
            sub = S[i:i+2]
            enc1+=sub[1]+sub[0]
        else:
            enc1+=S[-1]
    else:
        for i in range(0,N-1,2):
            sub = S[i:i+2]
            enc1+=sub[1]+sub[0]
    
    
    f_half = "abcdefghijklm"
    s_half = "nopqrstuvwxyz"
    s_half = s_half[::-1]
    for i in enc1:
        if i in f_half:
            enc2+= s_half[f_half.index(i)]
        else:
            enc2+= f_half[s_half.index(i)]
    print(enc2)
