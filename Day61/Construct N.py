T = int(input())
for i in range(T):
    N = int(input())
    if (N%7)%2 != 0 and N < 7 :
        print("No")
    else:
        print("Yes")
    
