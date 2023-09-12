for T in range(int(input())):
    string = input()
    res = "Sad"
    for i in range(len(string)-2):
        if string[i] in ['a','e','i','o','u']:
            if string[i+1] in ['a','e','i','o','u']:
                if string[i+2] in ['a','e','i','o','u']:
                    res = "Happy"
                    break
    print(res)
            
