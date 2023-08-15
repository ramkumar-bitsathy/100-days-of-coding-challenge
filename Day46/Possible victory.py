R,O,C = map(int,input().split())
rem_overs = 20-O
if C+(rem_overs*36) > R:
    print("Yes")
else:
    print("NO")
