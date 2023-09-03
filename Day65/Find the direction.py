for T in range(int(input())):
    N = int(input())
    if N%4 == 1:
        print("East")
    elif N%4 == 2:
        print("South")
    elif N%4 == 3:
        print("West")
    else:
        print("North")
