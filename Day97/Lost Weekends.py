for T in range(int(input())):
    A = list(map(int,input().split()))
    P = A.pop()
    if sum(A)*P <= 24*5:
        print("No")
    else:
        print("Yes")
