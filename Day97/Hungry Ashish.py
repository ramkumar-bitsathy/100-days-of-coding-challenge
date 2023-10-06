for T in range(int(input())):
    tot,pizz,burg = map(int,input().split())
    if pizz<=tot or (pizz<tot and burg<tot):
        print("Pizza")
    elif burg<=tot:
        print("Burger")
    else:
        print("Nothing")
