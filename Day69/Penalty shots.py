for T in range(int(input())):
    A1,A2,A3,A4,A5,A6,A7,A8,A9,A10 = map(int,input().split())
    team_1 = [A1,A3,A5,A7,A9]
    team_2 = [A2,A4,A6,A8,A10]
    if team_1.count(1) > team_2.count(1) :
        print(1)
    elif team_1.count(1) < team_2.count(1):
        print(2)
    else:
        print(0)
