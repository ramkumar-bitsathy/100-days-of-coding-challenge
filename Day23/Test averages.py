T = int(input())

def avg(a,b):
    average = (a+b)/2
    return average
    
for i in range(T):
    A,B,C = map(int,input().split())
    if avg(A,B)<35:
        print("Fail")
    elif avg(B,C)<35:
        print("Fail")
    elif avg(C,A)<35:
        print("Fail")
    else:
        print("Pass")
