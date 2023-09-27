for T in range(int(input())):
    N,X = map(int,input().split())
    if N%2==0 or X%2!=0 :
        print("YES")
    else:
        print("NO")
            
