T = int(input())
for i in range(T):
    A,B,C = input().split()
    A,B,C = int(A),int(B),int(C)
    if ((A+B) %2) != 0:
        print("YEs")
    elif ((B+C) %2) != 0:
        print("Yes")
    elif ((C+A) %2) != 0:
        print("Yes")
    else:
        print("NO")
      
