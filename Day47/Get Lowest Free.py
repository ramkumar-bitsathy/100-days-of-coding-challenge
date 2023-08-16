T = int(input())
for i in range(T):
    fee_lst = list(map(int,input().split()))
    fee_lst.remove(min(fee_lst))
    print(sum(fee_lst))
    
