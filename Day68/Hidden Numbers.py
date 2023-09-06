for T in range(int(input())):
    N = int(input())
    if N<=9:
        print(1,N)
    else:
        if N%2 == 0:
            print(2,N//2)
        else:
            print(1,N)
