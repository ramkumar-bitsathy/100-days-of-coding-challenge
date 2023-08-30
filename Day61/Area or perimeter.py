L = int(input())
B = int(input())
if ((2*L)+(2*B)) == (L*B):
    print("Eq")
    print(L*B)
elif ((2*L)+(2*B)) > (L*B):
    print("Peri")
    print((2*L)+(2*B))
elif ((2*L)+(2*B)) < (L*B):
    print("Area")
    print(L*B)
    
