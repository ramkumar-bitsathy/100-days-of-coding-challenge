T = int(input())
for i in range(T):
    N = int(input())
    cpy = N
    rev = 0
    while N>0:
        rem = N%10
        rev = (rev*10)+rem
        N//=10
    if rev == cpy:
        print("wins")
    else:
        print("loses")
        
