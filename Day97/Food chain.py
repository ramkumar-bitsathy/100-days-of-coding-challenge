for T in range(int(input())):
    A,B = map(int,input().split())
    count = 1 
    while A>=B:
        A = A//B 
        count+=1
    print(count)
