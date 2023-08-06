T = int(input())  

for _ in range(T):
    X, Y, Z = map(int, input().split())  
    time_for_x_lvls = X * Y  
    breaks = X // 3  
    tot_time = time_for_x_lvls + breaks * Z  
    if X % 3 == 0:
        tot_time -= Z
    print(tot_time)  
