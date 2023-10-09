for T in range(int(input())):
    A,B,C = map(int,input().split())
   
    if (abs(A-B)/2) % C == 0:
        print("YES")
    else:
        print("NO")
