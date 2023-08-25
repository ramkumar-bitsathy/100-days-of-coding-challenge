T = int(input())
for i in range(T):
    base = int(input())
    if base < 1500:
        print(base+ 0.1*base +0.9*base)
    elif base >= 1500:
        print(base+ 500 + 0.98*base)
