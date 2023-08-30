N = int(input())
highest_divisor = 0
for i in range(1,11):
    if N%i == 0:
        highest_divisor=i
print(highest_divisor)
    
