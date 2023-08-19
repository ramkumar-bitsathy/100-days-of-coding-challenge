T = int(input())
for i in range(T):
    a1,a2,a3,b1,b2,b3 = map(int,input().split())
    alice = [a1,a2,a3]
    bob = [b1,b2,b3]
    alice.remove(min(alice))
    bob.remove(min(bob))
    score1 = sum(alice)
    score2 = sum(bob)g
    if score2>score1:
        print("Bob")
    elif score1>score2:
        print("Alice")
    else:
        print("Tie")
    
