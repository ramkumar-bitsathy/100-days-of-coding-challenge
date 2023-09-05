for T in range(int(input())):
    N = int(input())
    Alice = list(map(int,input().split()))
    Bob = list(map(int,input().split()))
    happy = 0
    for i in range(N):
        if Alice[i]*2 < Bob[i]:
            continue
        elif Bob[i]*2 < Alice[i]:
            continue
        else:
            happy += 1 
    print(happy)
