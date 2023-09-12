for T in range(int(input())):
    n = 4
    Dict = dict(input().split() for i in range(n))
    if(Dict['Barcelona']>Dict['Eibar'] and Dict['RealMadrid']<Dict['Malaga']):
        print("Barcelona")
    else:
        print("RealMadrid")
    
    
    
