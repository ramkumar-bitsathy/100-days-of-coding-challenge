T = int(input())
for i in range(T):
    N,X,P = map(int,input().split())
    correct = X
    incorrect = N-X
    tot_marks = (correct*3) + (incorrect*(-1))
    if tot_marks>=P:
        print("Pass")
    else:
        print("Fail")
