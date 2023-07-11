T = int(input())
for i in range(T):
    A,B,C = input().split()
    A,B,C = int(A),int(B),int(C)
    if sum([A,B])== C or sum([B,C])== A or sum([C,A])==B:
        print("Yes")
    else:
        print("NO")
