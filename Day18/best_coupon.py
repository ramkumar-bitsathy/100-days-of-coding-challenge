# cook your dish here
T = int(input())
for i in range(T):
    X = int(input())
    off = X*0.1
    flat = 100
    if off > flat:
        print(int(off))
    else:
        print(100)
    
