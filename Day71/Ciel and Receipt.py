for T in range(int(input())):
    P = int(input())
    lst = [2**x for x in range(0,12)]
    i = len(lst)-1
    count = 0
    while P!=0 and i >=0:
        if lst[i] >P:
            i-=1
        else:
            P = P-lst[i]
            count +=1
    print(count)
        
    
