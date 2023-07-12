T = int(input())
for i in range(T):
    W,X,Y,Z = input().split()
    i_vol , Max_capacity , Lit_per_hr , no_of_hrs = int(W),int(X),int(Y),int(Z)
    volume = i_vol+ (Lit_per_hr * no_of_hrs)
    if volume > Max_capacity:
        print("overflow")
    elif volume < Max_capacity:
        print("unfilled")
    else:
        print("filled ")
