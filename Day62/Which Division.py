T = int(input())
for i in range(T):
    R = int(input())
    if 2000<=R:
        print(1)
    elif 1600<=R<2000:
        print(2)
    elif R<1600:
        print(3)
