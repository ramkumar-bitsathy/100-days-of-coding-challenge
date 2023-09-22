for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    count1 = 0
    count2 = 0
    om_streak = count1
    addy_streak = count2
    for i in range(N):
        if A[i] != 0:
            count1+=1 
        else:
            count1 = 0
        if B[i] !=0:
            count2 +=1 
        else:
            count2 = 0
        om_streak = max(count1, om_streak)
        addy_streak = max(count2, addy_streak)
    if addy_streak<om_streak:
        print("Om")
    elif om_streak==addy_streak:
        print("Draw")
    else:
        print("Addy")
