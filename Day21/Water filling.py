T = int(input())
for i in range(T):
    B1,B2,B3 = input().split()
    B = [int(B1),int(B2),int(B3)]
    if B.count(0) >=2:
        print("Water filling time")
    else: 
        print("Not now")
    
