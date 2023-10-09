def pseudo_sort(B):
    for i in range(len(B)-1):
        if B[i]>B[i+1]:
            B[i+1],B[i] = B[i],B[i+1]
            break
    return B 

for T in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    if pseudo_sort(A) == sorted(A):
        print("YES")
    else:
        print("NO")
