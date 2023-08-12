T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    score_for_A = 500
    score_for_B = 1000
    
    prob1 = (score_for_A - X*2) + (score_for_B - (X+Y)*4)
    prob2 = (score_for_A - Y*4) + (score_for_B - (X+Y)*2)
    
    if prob2>prob1:
        print(prob2)
    else:
        print(prob1)
