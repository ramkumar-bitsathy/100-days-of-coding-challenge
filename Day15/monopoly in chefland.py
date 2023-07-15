T = int(input())
for i in range(T):
    R1,R2,R3 = input().split()
    rev_list = [int(R1),int(R2),int(R3)]
    if rev_list[0] > rev_list[1]+rev_list[2]:
        print("Yes")
    elif  rev_list[1] > rev_list[0]+rev_list[2]:
        print("Yes")
    elif rev_list[2] > rev_list[0]+rev_list[1]:
        print("Yes")
    else:
        print("no")
        
