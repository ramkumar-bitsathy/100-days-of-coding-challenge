T = int(input())
for i in range(T):
    M, H = map(int, input().split())
    BMI = M/ (H**2)
    if BMI <= 18:
        print(1)
    elif BMI <= 24:
        print(2)
    elif BMI <= 29:
        print(3)
    else:
        print(4)
