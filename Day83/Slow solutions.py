import math
t=int(input())
for T in range(t):
    x,y,z=map(int,input().split())
    c=x*y
    if(c>=z):
      a=z//y
      k=y*a 
      g=z-k
      result=(a*y*y)+g*g
      print(result)
    else:
        print(x*y*y)
    
