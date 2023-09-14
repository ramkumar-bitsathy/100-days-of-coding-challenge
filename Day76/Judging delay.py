for T in range(int(input())):
    count = 0
    for i in range(int(input())):
        A,B = map(int,input().split())
        if abs(A-B) >5:
            count+=1
    print(count)
        
