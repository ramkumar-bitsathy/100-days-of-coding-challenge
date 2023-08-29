T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    mini = min(A,B)
    maxi = max(A,B)
    res = ""
    for j in range(50):
        if mini == maxi:
            res = "yes"
        elif mini > maxi:
            break
        else:
            res = "no"
            
        mini = mini*2
    print(res)
    
