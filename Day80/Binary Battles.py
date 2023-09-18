import math
for T in range(int(input())):
    N, A, B = map(int, input().split())
    num_rounds = int(math.log2(N))
    Time = num_rounds * A
    Break = (num_rounds - 1) * B
    print(Time + Break)
