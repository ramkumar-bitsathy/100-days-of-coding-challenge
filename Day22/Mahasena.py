T = int(input())
S = [int(x) for x in input().split()]
even_count = 0
odd_count = 0
for i in S:
    if i%2 == 0:
        even_count+= 1
    elif i%2 !=0:
        odd_count += 1
        
if even_count > odd_count:
    print("READY FOR BATTLE")
else: 
    print("NOT READY")
    
    
    
