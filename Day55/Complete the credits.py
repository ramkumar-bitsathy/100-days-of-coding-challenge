T = int(input())
for i in range(T):
    N = int(input())
    if N>65:
        print("Overload")
    elif N<35:
        print("Underload")
    else:
        print("Normal")
