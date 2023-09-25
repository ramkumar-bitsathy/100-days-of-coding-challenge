for T in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    c = 0
    for i in arr:
        k=arr.count(i)
        if k>=3:
            c+=1
    if c>1:
        print("NO")
    else:
        print("yes")
