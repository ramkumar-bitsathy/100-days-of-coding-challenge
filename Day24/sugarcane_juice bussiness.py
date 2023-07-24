import math
T = int(input())
for i in range(T):
    N = int(input())
    total_amount = N*50
    spends = total_amount*(70/100)
    profit = total_amount- math.ceil(spends)
    print(int(profit))
