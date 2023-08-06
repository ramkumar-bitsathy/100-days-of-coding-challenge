T = int(input())
for i in range(T):
    N = int(input())
    Na,Nb,Nc,Nd = map(int,input().split())
    lst = list([Na,Nb,Nc,Nd])
    print(max(lst))
