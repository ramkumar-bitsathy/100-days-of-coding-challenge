T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    copy = S 
    first_half = S[0:N//2]
    second_half = S[N//2:N+1]
    if copy == (second_half+first_half):
        print("Yes")
    else:
        print("NO")
