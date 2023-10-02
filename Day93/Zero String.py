for T in range(int(input())):
    N = int(input())
    S = input()
    one = S.count("1")
    zero = S.count("0")
    if zero>=one:
        val=one
    else:
        val=1+zero
    print(val)
