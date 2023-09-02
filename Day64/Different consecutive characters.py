for T in range(int(input())):
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if i == len(S)-1:
            break
        if S[i] == S[i+1]:
            count+=1
    print(count)
