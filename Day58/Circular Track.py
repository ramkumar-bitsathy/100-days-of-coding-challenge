T = int(input())
for i in range(T):
    A,B,M = map(int,input().split())
    F = abs(A-B)
    print(min(F,M-F))
