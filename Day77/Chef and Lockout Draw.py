for T in range(int(input())):
    lst=list(map(int,input().split()))
    lst.sort()
    if lst[0]+lst[1]==lst[2]:
        print("yes")
    else:
        print("no")
