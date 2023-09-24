import math
for T in range(int(input())):
    N = int(input())
    types = []
    for i in range(N):
        a= int(input())
        types.append(a)
    for j in types:
        if types.count(j)%2 == 1:
            print(j)
            break
