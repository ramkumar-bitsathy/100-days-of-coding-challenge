T = int(input())
for i in range(T):
    N = int(input())
    divisor_count = 0
    for i in range(1,N+1):
        if (N%i)==0:
            divisor_count +=1
    if divisor_count == 2:
        print("yes")
    else:
        print("no")
