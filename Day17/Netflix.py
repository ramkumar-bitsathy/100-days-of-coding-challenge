T = int(input())
for i in range(T):
    A,B,C,X = input().split()
    alice , bob, charlie, subscription = int(A),int(B),int(C),int(X)
    if alice + bob >= subscription:
        print("yes")
    elif bob+charlie >= subscription:
        print("Yes")
    elif charlie+alice >= subscription:
        print("Yes")
    else:
        print("NO")
