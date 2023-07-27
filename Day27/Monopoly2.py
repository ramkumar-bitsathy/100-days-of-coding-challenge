def sum_all(*a):
  sum = 0
  for i in a:
    sum+=i
  return sum
  
T = int(input())
for i in range(T):
    P,Q,R,S = map(int,input().split())
    if P > sum_all(Q,R,S):
        print("Yes")
    elif Q > sum_all(P,R,S):
        print("Yes")
    elif R > sum_all(P,Q,S):
        print("Yes")
    elif S > sum_all(P,Q,R):
        print("Yes")
    else:
        print("NO")
