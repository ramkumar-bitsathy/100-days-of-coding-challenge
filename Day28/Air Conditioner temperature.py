T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    count = 0
    for N in range(1,101,1):
        if N>=A and N<=B and N>=C:
            count +=1
    if count!=0:
        print("YES")
    else:
        print("NO")
