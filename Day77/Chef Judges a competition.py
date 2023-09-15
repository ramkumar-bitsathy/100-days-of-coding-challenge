for T in range(int(input())):
    N = int(input())
    alice = list(map(int,input().split()))
    bob = list(map(int,input().split()))
    a_score = sum(alice) - max(alice)
    b_score = sum(bob) - max(bob)
    if a_score>b_score:
        print("Bob")
    elif a_score<b_score:
        print("Alice")
    else:
        print("Draw")
