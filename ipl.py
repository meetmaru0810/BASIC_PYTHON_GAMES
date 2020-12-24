def computer_bat():
    score1=0
    wicket=0
    for i in range(1,11):
        input()
        bat_1=random.choice(l2)
        if bat_1=="wicket":
            print("-----out-----")
            wicket+=1
        else:
            if bat_1==6:
                print("------SIXER------")
            elif bat_1==4:
                print("------FOUR------")
            score1+=bat_1
        

        print(OPP_TEAM ,"score",score1,"/",wicket," ",i," ball")
   

    return score1

def user_bat():
    score2=0
    wicket=0
    bat_1=random.choice(l2)
    for j in range(1,11):
        input()
        if bat_1=="wicket":
            print("-----out-----")
            wicket+=1
        else:
            if bat_1==6:
                print("------SIXER------")
            elif bat_1==4:
                print("------FOUR------")
            score2+=bat_1
            

        print(MY_TEAM ,"score",score2,"/",wicket," ",j," ball")
   
    return score2

import random
l1=["mumbai","delhi","KKR","RCB"]
MY_TEAM="PANJAB"
OPP_TEAM=random.choice(l1)
print(MY_TEAM," vs ",OPP_TEAM)
l2=[0,1,2,4,6,"wicket"]

print("                                        TOSS TIME")
TOSS=["head","tail"]
user_toss=input("head or tail:")
v=random.choice(TOSS)
print(v)

if v==user_toss:
    print(MY_TEAM,"has won the toss")
    print("you have to bat or ball")
    b=input()
    if b=="bat":
        print(MY_TEAM," has won the toss and chose batting")
        print("-----------------------FOR START THE GAME PLS PRESS ENTER -------------------------------------------------")
        s2=user_bat()
        print("----------------------------CHANCE TO PLAY OTHER TEAM PLS PRESS ENTER------------------------------------------------------")
        input() 
        s1=computer_bat()
        if s1>s2:
            how_many_run=s1-s2
            print("----------------",OPP_TEAM," HAS WON THE MATCH by ",how_many_run,"runs---------------")
        else:
            how_many_run=s2-s1
            print("----------------",MY_TEAM,"HAS WON THE MATCH by ",how_many_run,"runs--------------")

    elif b=="ball":
        print(MY_TEAM,"has won the toss and chose balling")
        print("-----------------------FOR START THE GAME PLS PRESS ENTER -------------------------------------------------")
        s1=computer_bat()
        print("----------------------------CHANCE TO PLAY OTHER TEAM PLS PRESS ENTER------------------------------------------------------")
        input() 
        s2=user_bat()
        if s1>s2:
            how_many_run=s1-s2
            print("----------------",OPP_TEAM," HAS WON THE MATCH by ",how_many_run,"runs---------------")
        else:
            how_many_run=s2-s1
            print("----------------",MY_TEAM,"HAS WON THE MATCH by ",how_many_run,"runs--------------")

else:
    print(OPP_TEAM ,"have won the toss")
    bob=["bat","ball"]
    b1=random.choice(bob)
    if b1=="bat":
        print(OPP_TEAM,"choose bat")
        print("-----------------------FOR START THE GAME PLS PRESS ENTER -------------------------------------------------")
        s1=computer_bat()
        print("----------------------------CHANCE TO PLAY OTHER TEAM PLS PRESS ENTER------------------------------------------------------")
        input() 
        s2=user_bat()
        if s1>s2:
            how_many_run=s1-s2
            print("----------------",OPP_TEAM," HAS WON THE MATCH by ",how_many_run,"runs---------------")
        else:
            how_many_run=s2-s1
            print("----------------",MY_TEAM,"HAS WON THE MATCH by ",how_many_run,"runs--------------")

    else:
        print(OPP_TEAM,"choose ball")
        print("-----------------------FOR START THE GAME PLS PRESS ENTER -------------------------------------------------")
        s2=user_bat()
        print("----------------------------CHANCE TO PLAY OTHER TEAM PLS PRESS ENTER------------------------------------------------------")
        input() 
        s1=computer_bat()
        if s1>s2:
            how_many_run=s1-s2
            print("----------------",OPP_TEAM," HAS WON THE MATCH by ",how_many_run,"runs---------------")
        else:
            how_many_run=s2-s1
            print("----------------",MY_TEAM,"HAS WON THE MATCH by ",how_many_run,"runs--------------")



