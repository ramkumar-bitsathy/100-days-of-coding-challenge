import math
T = int(input())
for i in range(T):
    B,L = map(int,input().split())
    R1 = math.sqrt((L**2)+(B**2))
    R2 = math.sqrt((L**2)-(B**2))
    print(round(R2,4),round(R1,4))
