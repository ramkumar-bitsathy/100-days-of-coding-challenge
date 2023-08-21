poly=int(input())
for p in range(poly):
  n=int(input())
  a=list(map(int,input().split()))
  deg=0
  for i in range(len(a)):
    if a[i]!=0 and i>deg: deg=i
  print(deg)
