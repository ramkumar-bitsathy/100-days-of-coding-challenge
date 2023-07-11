T = int(input())
for i in range(T):
    x,y,z = input().split()
    sec_1 , sec_2, sec_3 = int(x),int(y),int(z)
    tot_score = sec_1 + sec_2 + sec_3
    if tot_score>=100  and sec_1 >=10 and sec_2>=10 and sec_3>=10:
        print("Pass")
    else:
        print("Fail")
