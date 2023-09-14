for T in range(int(input())):
    row,column = map(int,input().split())
    if row%2==0 and column%2==0:
        print(0)
    elif row%2!=0 and column%2!=0:
        print(row+column-1)
    elif row%2==0 and column%2!=0:
        print(row)
    else:
        print(column)
