T = int(input())
for i in range(T):
    a,b,c,d = map(int,input().split())
    first_Set = [a,b] 
    second_set = [c,d]
    print(max(first_Set)+ max(second_set))
