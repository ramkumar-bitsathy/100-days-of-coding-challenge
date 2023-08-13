T = int(input())
for i in range(T):
    A,B,X,Y = map(int,input().split())
    time_a = A/X 
    time_b = B/Y
    if time_b>time_a:
        print("Chef")
    elif time_a>time_b:
        print("Chefina")
    else:
        print("Both")
