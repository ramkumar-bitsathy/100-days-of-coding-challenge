for T in range(int(input())):
    s = input()
    for i in range(0,len(s)-1,2):
        if s[i]==s[i+1]:
            print("no") 
            break
    else:
    
        print("yes")
        
