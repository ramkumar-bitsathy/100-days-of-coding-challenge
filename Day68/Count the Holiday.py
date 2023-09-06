for T in range(int(input())):
        N=int(input())
        lst=list(map(int,input().split()))
        sat=[6,13,20,27]
        sun=[7,14,21,28]
        print(len(set(lst+sat+sun)))
