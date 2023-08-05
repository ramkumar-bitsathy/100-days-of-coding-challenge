N = int(input())
val = []
for i in range(N):
    val.append(int(input()))
sorted_lst = sorted(val,reverse = False)
for j in sorted_lst:
    print(j)
