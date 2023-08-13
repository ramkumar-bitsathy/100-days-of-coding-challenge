T = int(input())
for i in range(T):
    P = int(input())
    No_of_problems = (P//100)+ (P%100)
    if No_of_problems <=10:
        print(No_of_problems)
    else:
        print(-1)
