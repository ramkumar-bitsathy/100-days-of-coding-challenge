import math
T = int(input())
for i in range(T):
    X = int(input())
    correctly = math.ceil(X/3)
    #print(correctly)
    incorrectly = (correctly * 3)-X
    print(incorrectly)
