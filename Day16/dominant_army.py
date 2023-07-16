T = int(input())
for i in range(T):
    Na,Nb,Nc = input().split()
    Na,Nb,Nc = int(Na),int(Nb),int(Nc)
    dominant = False
    if Na > Nb+Nc:
        dominant = True
    elif Nb > Nc+Na:
        dominant = True
    elif Nc > Nb+Na:
        dominant = True
    if dominant == True:
        print("Yes")
    else:
        print("No")
