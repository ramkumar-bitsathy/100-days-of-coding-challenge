T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    initial_left_shoe = M 
    initial_right_shoe = 0
    no_of_pairs = N
    if initial_left_shoe>= no_of_pairs:
        left_shoe_to_buy = 0
    elif initial_left_shoe <no_of_pairs:
        left_shoe_to_buy = no_of_pairs-initial_left_shoe
    right_shoe_to_buy = N 
    print(left_shoe_to_buy+right_shoe_to_buy)
    
