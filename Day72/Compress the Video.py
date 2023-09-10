for T in range(int(input())):
    N = int(input())
    frames = list(map(int,input().split()))
    m=1
    for i in range(0,N-1):
        if frames[i]!=frames[i+1]:
            m+=1
    print(m)
