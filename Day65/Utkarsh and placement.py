for T in range(int(input())):
    one , two, three = map(str,input().split())
    x,y = map(str,input().split())
    if one in (x,y):
        print(one)
    elif two in (x,y):
        print(two)
    else:
        print(three)
