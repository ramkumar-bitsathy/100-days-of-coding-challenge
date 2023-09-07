for T in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    arr = list(set(arr))
    fir_max = max(arr)
    arr.remove(fir_max)
    sec_max = max(arr)
    print(fir_max+sec_max)
    
