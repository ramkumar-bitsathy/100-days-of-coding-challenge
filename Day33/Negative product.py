T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    if A*B <0:
        print("YES")
    elif B*C <0:
        print("YES")
    elif C*A <0:
        print("YES")
    else:
        print("NO")
