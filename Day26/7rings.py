T = int(input())

def is_valid(num):
    if len(str(num))==4:
        return "NO"
    elif len(str(num))==5 and (num//10000) != 0:
        return "yes"
    else:
        return "no"
        
for i in range(T):
    N,X = map(int,input().split())
    bill = N*X 
    print(is_valid(bill))
    
