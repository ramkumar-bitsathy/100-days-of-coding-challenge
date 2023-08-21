T = int(input())
for i in range(T):
    N = int(input())
    lst = list(input().split())
    start_count = 0
    ltime_Count = 0
    for item in lst:
        if item == "START38":
            start_count+=1
        elif item == "LTIME108":
            ltime_Count+=1
    print(start_count,ltime_Count)
