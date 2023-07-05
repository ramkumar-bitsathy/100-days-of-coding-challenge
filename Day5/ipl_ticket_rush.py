"""
Problem:
DAIICT college students want to attend an IPL match. A total of N students from the college want to go while only 
M tickets are available for the match. Determine how many students won't be able to book tickets.

Input Format:
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers N and M — the number of students wants to go and the total number of tickets available, respectively.
"""

T = int(input())
for i in range(T):
    N,M = input().split()
    stud,tkt = int(N),int(M)
    if stud < tkt:
        print(0)
    else:
        print(stud-tkt)
