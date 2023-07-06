"""
Problem:
Chef's dog binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).
If Chef's commands have a frequency of X Hertz, find whether binary can hear them or not.

Input Format:
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single integer X - the frequency of Chef's commands in Hertz.
"""

T = int(input())
for i in range(T):
    X = int(input())
    if 67<=X<=45000:
        print("YES")
    else:
        print("NO")
