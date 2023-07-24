T = int(input())
for i in range(T):
    A,B,X,Y = map(int,input().split())
    unit, year, gram, can_produce = A,B,X,Y
    produced = gram*can_produce
    should = unit*year
    if produced>=should:
        print("Yes")
    else:
        print("No")
