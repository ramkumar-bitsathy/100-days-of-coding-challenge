for T in range(int(input())):
    X = int(input())
    string = input()
    chef_win = string.count('N')
    carlson_win = string.count('C')
    draw = string.count("D")
    if chef_win > carlson_win:
        print(40*X)
    elif chef_win< carlson_win:
        print(60*X)
    else:
        print(55*X)
