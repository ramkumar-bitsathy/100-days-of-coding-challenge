T = int(input())
for i in range(T):
    N = list(map(int,input().split()))
    sunny = N.count(1)
    rainy = N.count(0)
    if sunny>rainy:
        print("Yes")
    else:
        print("No")
