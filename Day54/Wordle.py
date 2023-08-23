T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    new_str = ''
    if len(str1) == len(str2):
        for j in range(len(str1)):
            if str1[j] == str2[j]:
                new_str+="G"
            else:
                new_str+="B"
    print(new_str)
