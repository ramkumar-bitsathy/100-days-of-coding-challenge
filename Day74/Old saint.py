for T in range(int(input())):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if A.count(1) == B.count(1):
        print("Pass")
    else:
        print("Fail")
        
    
