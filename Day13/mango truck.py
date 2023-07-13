T = int(input())
for i in range(T):
    X,Y,Z = input().split()
    w_mang, w_truck, w_withstd  = int(X),int(Y),int(Z)
    no_mangoes = 0
    for i in range(0,100,1):
        if w_truck + w_mang*i <= w_withstd:
            no_mangoes = i
    
    print(no_mangoes)      
        
