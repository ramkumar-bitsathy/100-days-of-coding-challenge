bet=int(input())
for t in range(bet):
  Sa,Sb,Sc=map(int,input().split())
  if min(Sa,Sb,Sc)==Sa:
    print("Draw")
  else:
    print("Bob") if min(Sa,Sb,Sc)==Sb else print("Alice")
