"""
Problem:
King loves to go on tours with his friends.King has N cars that can seat 5 people each and M cars that can seat 
7 people each. Determine the maximum number of people that can travel together in these cars.

Input Format:
The first line of input contains a single integer T, the number of test cases.
The first and only line of each test case contains two space-separated integers N and M — the number of 5-seaters and 
7-seaters, respectively.
"""

T = int(input())
for i in range(T):
    X,Y = input().split()
    N,M = int(X),int(Y)
    print((N*5)+(M*7))
