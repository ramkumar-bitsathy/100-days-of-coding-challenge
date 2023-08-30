T = int(input())
for i in range(T):
    Z,Y,A,B,C = map(int,input().split())
    bal = Z-Y
    if bal-A-B-C >=0:
        print("YES")
    else:
        print("NO")
