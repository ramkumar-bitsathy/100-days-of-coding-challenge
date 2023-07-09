T = int(input())
for i in range(T):
    X,Y,Z = input().split()
    five , ten , cost = int(X),int(Y),int(Z)
    total_amount = five*5 + ten*10
    num_chocolates = total_amount // cost
    print(num_chocolates)
