"""
Problem:
Chef is fond of burgers and decided to make as many burgers as possible.Chef has A patties and B buns. To make 1 burger, Chef needs 
1 patty and 1 bun.Find the maximum number of burgers that Chef can make.
"""

T = int(input())
for i in range(T):
    pattie,bun = input().split()
    pattie,bun = int(pattie),int(bun)
    if pattie<bun:
        print(pattie)
    else: 
        print(bun)
