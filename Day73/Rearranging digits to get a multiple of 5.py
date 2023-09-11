for T in range(int(input())):
    N = int(input())
    num = int(input())
    if str(num).count('0')>0 or str(num).count('5')>0:
        print("YES")
    else:
        print("NO")
