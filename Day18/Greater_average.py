T = int(input())
for i in range(T):
    A,B,C = input().split()
    A,B,C = int(A),int(B),int(C)
    average_a_b = (A+B)/2
    if average_a_b>C:
        print("YES")
    else:
        print("NO")
