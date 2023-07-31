#difficulty rating: 613
LD_double = list(range(1,11))
LD_single = list(range(11,16))
UD_double = list(range(16,26))
UD_single = list(range(26,31))

T = int(input())
for i in range(T):
    N = int(input())
    if N in LD_single:
        print("Lower single")
    elif N in LD_double:
        print("Lower Double")
    elif N in UD_single:
        print("Upper Single")
    elif N in UD_double:
        print("Upper Double")
