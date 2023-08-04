T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    new_str = ""
    dictionary = {'A':'T','T':'A','C':'G','G':'C'}
    for i in range(0,N):
        new_str+= dictionary[S[i]]
    print(new_str)
        
        
