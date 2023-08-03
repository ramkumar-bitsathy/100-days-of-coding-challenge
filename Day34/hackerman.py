def check_prime(N):
    count = 0
    for i in range(1,N+1):
        if N%i == 0:
          count+=1
    if count == 2:
        return "prime"
    else:
        return None
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    if check_prime(A+B) == "prime":
        print("Alice")
    else: 
        print("Bob")
