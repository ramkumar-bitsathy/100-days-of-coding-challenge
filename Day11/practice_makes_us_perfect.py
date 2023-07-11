p1,p2,p3,p4 = input().split()
P = [int(p1),int(p2),int(p3),int(p4)]
count = 0
for i in P:
    if i>=10:
        count+=1
    
print(count)

