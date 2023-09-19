for T in range(int(input())):
    N = int(input())
    S = input()
    if N<=3:
        print("YES")
    else:
        for i in range(N-3):
            string = S[i:i+4]
            vow1 = 'a' in string or 'e' in string or 'i' in string 
            vow2 = 'o' in string or 'u' in string 
            if not vow1 and not vow2:
                print("NO")
                break 
        else:
            print("YES")
        
    
        
