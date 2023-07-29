import math
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    if math.ceil(100-(100*(A/100))) < math.ceil(200 - (200*(B/100))):
        print("First")
    elif math.ceil(100-(100*(A/100))) > math.ceil(200 - (200*(B/100))):
        print("Second")
    elif math.ceil(100-(100*(A/100))) == math.ceil(200 - (200*(B/100))):
        print("BOTH")
