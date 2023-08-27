T = int(input())
for i in range(T):
    H,C,T = map(int,input().split())
    Hi,Ci,Ti = 50,0.7,5600
    grade = 0
    if H>Hi and C<Ci and T>Ti:
        grade = 10
    elif H>Hi and C<Ci and T<=Ti:
        grade = 9
    elif H<=Hi and C<Ci and T>Ti:
        grade = 8
    elif H>Hi and C>=Ci and T>Ti:
        grade = 7
    elif [H>Hi,C<Ci,T>Ti].count(True) ==1:
        grade = 6
    elif [H>Hi,C<Ci,T>Ti].count(False) ==3:
        grade = 5
    print(grade)
