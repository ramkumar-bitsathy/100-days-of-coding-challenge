T = int(input())
for i in range(T):
    N,X = input().split()
    N,X = int(N),int(X)
    loop_dur = X*3
    complete_loop = N// loop_dur
    print(complete_loop)
        
