for T in range(int(input())):
    N,B = map(int,input().split())
    
    selection = []  
    for i in range(N):
        det = list(map(int, input().split()))
        
        if det[2] <= B: 
            selection.append(det[0]*det[1])
    
    if len(selection) == 0:
        print("no tablet")
    else:
        print(max(selection))
            
