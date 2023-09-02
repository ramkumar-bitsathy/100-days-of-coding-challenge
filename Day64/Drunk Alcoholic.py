for T in range(int(input())):
    k = int(input())
    step = 0
    for i in range(1,k+1):
        if i%2 == 0:
            step-=1
        elif i%2 !=0:
            step+=3
    print(step)
