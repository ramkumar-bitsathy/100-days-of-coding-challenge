for T in range(int(input())):
    N = int(input())
    B = input()
    present = B.count('1')
    absent = B.count('0')
    min_days = 120*(75/100)
    if (120-N)+present >= min_days:
        print("YES")
    else:
        print("NO")
        
    
