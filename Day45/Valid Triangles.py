T = int(input())
for i in range(T):
    lst = list(map(int,input().split()))
    sum_angles = sum(lst)
    if sum_angles==180:
        print("YES")
    else:
        print("NO")
