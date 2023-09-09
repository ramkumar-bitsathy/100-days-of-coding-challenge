N,H,x = map(int,input().split())
zones = list(map(int,input().split()))
sol = "NO"
for i in zones:
    if i+x >=H:
        sol = "yes"
        break
print(sol)        
    
