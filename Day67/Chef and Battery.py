for T in range(int(input())):
    N = int(input())
    time = 0
    while N!=50:
        if N<50:
            N+=2
        elif N>50:
            N-=3
        time+=1 
    print(time)
