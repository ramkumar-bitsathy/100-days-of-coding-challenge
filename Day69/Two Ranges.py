for T in range(int(input())):
    A,B,C,D = map(int,input().split())
    range1 = list(range(A,B+1))
    range2 = list(range(C,D+1))
    print(len(set(range1+range2)))
