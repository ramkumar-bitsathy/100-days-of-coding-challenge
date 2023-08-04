T = int(input())
for i in range(T):
    X = int(input())
    one = 'Huge'
    two = 'small'
    three = 'normal'
    if X<=3:
        if X==1:
            print(one)
        elif X==2:
            print(two)
        else:
            print(three)
    else:
        if X%3 ==1:
            print(one)
        elif X%3 == 2:
            print(two)
        else:
            print(three)
        
