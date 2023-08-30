T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    lst = list(map(int,input().split()))
    passed = list()
    for j in range(X):
        passed.append(max(lst))
        lst.remove(max(lst))
    print(min(passed)-1)
        
