N = int(input())
player1_lead = list()
player2_lead = list()
sc1 = 0
sc2 = 0
for i in range(N):
    a,b = map(int,input().split())
    sc1+=a
    sc2+=b
    if sc1>sc2:
        player1_lead.append(abs(sc1-sc2))
    elif sc1<sc2:
        player2_lead.append(abs(sc1-sc2))
if len(player1_lead)==0 :
    print(2,max(player2_lead))
elif len(player2_lead)==0:
    print(1,max(player1_lead))
elif max(player1_lead) > max(player2_lead):
    print(1,max(player1_lead))
else:
    print(2,max(player2_lead))
