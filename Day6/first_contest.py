"""
Now to the problem:

In a contest where N new users visited the contest,
A users just saw the problems and didn’t make any submissions and hence won’t get any rating.
B users who made a submission but could not solve any problem correctly. Thus, after the contest, they will get a rating in the range 800−1000.
Everyone else could correctly solve at least 1 problem. Thus, they will get a rating strictly greater than 1000 after the contest.
You need to output the number of new users in the contest who, after the contest, will get a rating and also the number of new users 
who will get a rating strictly greater than 1000.

Input Format
Each input file contains of a single line, with three integers ,N,A and 
B - the number of new users, the number of users who just saw the problem and didn't make any submission, 
and the number of users who made a submission but could not solve any problem correctly.
"""

N,A,B = input().split()
tot, no_sub , wrong_sub = int(N),int(A),int(B)
get_rating = tot - no_sub
couldnt_solve = get_rating - wrong_sub

print(get_rating,couldnt_solve)
