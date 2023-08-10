T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    online_cost = N - N*(10/100)
    offline_cost = M 
    if offline_cost>online_cost:
        print("ONLINE")
    elif offline_cost<online_cost:
        print("DINING")
    elif offline_cost==online_cost:
        print("EITHER")
    
