for T in range(int(input())):
    N,A,B = map(int,input().split())
    faces = list(map(int,input().split()))
    prob_a = faces.count(A)/N
    prob_b = faces.count(B)/N
    print(prob_b*prob_a)
