for T in range(int(input())):
    N,K = map(int,input().split())
    if K==0:
        if N%4 != 0 :
            print("On")
        else:
            print("Off")
    elif K==1:
        if N%4!=0:
            print("Ambiguous")
        else:
            print("On")
