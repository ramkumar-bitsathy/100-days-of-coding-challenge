T = int(input())
for _ in range(T):
    P, Q = map(int, input().split())
    
    total_points = P + Q
    total_serves = total_points // 2 
    
    if total_serves % 2 == 0:
        print("Alice")
    else:
        print("Bob")
    
