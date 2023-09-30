for T in range(int(input())):
    N = int(input())
    S = input()
    if N%2 != 0:
        print("NO")
    else:
        res = 0
        for i in range(N):
            if S.count(S[i])%2 == 0:
                res = 0
            else:
                res = 1
                break
        if res != 0:
            print("NO")
        else:
            print("YES")
