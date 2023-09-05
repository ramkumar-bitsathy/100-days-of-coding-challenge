for T in range(int(input())):
    PA,PB,PC = map(int,input().split())
    if PA+PC > PB:
        print(PA+PC)
    else:
        print(PB)
