for T in range(int(input())):
    S = input()
    new_str = ''
    for i in range(len(S)):
        if S[i] == '<':
            new_str += '>'
        elif S[i] == '>':
            new_str += '<'
        else:
            new_str += S[i]
    print(new_str.count('><'))
