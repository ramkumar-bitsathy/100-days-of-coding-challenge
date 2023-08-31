T = int(input())
for i in range(T):
    Q,P = map(int,input().split())
    if Q>1000:
        print(Q*(P-(P*0.1)))
    else:
        print(Q*P)
    
