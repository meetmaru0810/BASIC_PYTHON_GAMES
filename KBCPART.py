def q1():
    print("Q=1  Is Python case sensitive when dealing with identifiers?")
    print("a) yes")
    print("b) no")
    print("c) machine dependent")
    print("d) none of the mentioned")
def q2():
    print("Q=2 What is the maximum possible length of an identifier?")
    print("a) 31 characters")
    print("b) 63 characters")
    print("c) 79 characters")
    print("d) none of the mentioned")
def q3():
    print("Q=3 Which of the following is not a keyword?")
    print("a) eval")
    print("b)assert ")
    print("c)nonlocal ")
    print("d)pass ")
def q4():
    print("Q=4 Which of these in not a core data type?")
    print("a)Lists ")
    print("b)Dictionary")
    print("c)Tuples")
    print("d)Class ")
def q5():
    print("Q=5 Which of the following will run without errors?")
    print("a)round(45.8) ")
    print("b)round(6352.898,2,5) ")
    print("c)round() ")
    print("d)round(7463.123,2,1) ")
def q6():
    print("Q=6 What is the return type of function id?")
    print("a)INT ")
    print("b)FLOAT ")
    print("c)BOOL ")
    print("d)DICT ")
def q7():
    print("Q=7 What data type is the object below?")
    print("L = [1, 23, 'hello', 1]")
    print("a)list ")
    print("b)dict ")
    print("c)array ")
    print("d)tuple ")
def q8():
    print("Q=8 In order to store values in terms of key and value we use what core data type.")
    print("a)dict ")
    print("b)tuple ")
    print("c)list ")
    print("d)array ")
def q9():
    print("Q=9  What arithmetic operators cannot be used with strings?")
    print("a)+ ")
    print("b)* ")
    print("c)- ")
    print("d)all of above mention ")
def q10():
    print("Q=10 Which of the following commands will create a list?")
    print("a) list1 = list() ")
    print("b) list1 = []")
    print("c) list1 = list([1, 2, 3])")
    print("d)  all of the mentioned")


def kbc():
    global N
    
    print("press 1 for play")
    print("press 2 for quit")

    choice=int(input("enter the choice:"))
    if choice==1:
        play()
        # print("-------TOTAL POINT OF KBC ====:",total)
        # if total1==500:
        #     print("--------WINNING AMOUNT IS 5 LACS")
        
    elif choice==2:
        return False

total=0
def play():
    global total
    print("-------------------- WELCOME TO KBC ----------------------------------")
    q1()
    a1=input("Enter the a,b,c,d:")
    if a1=="a" or a1=="A":
        total=total+50
        RIGHT_Q.append("a1")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a1")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q2()
    a2=input("Enter the a,b,c,d:")
    if a2=="d" or a2=="D":
        total=total+50
        RIGHT_Q.append("a2")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a2")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q3()
    a3=input("Enter the a,b,c,d:")
    if a3=="a" or a3=="A":
        total=total+50
        RIGHT_Q.append("a3")
        print("your score:",total)
    else:
        total=total-20 
        WRONG_Q.append("a3")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q4()
    a4=input("Enter the a,b,c,d:")
    if a4=="d" or a4=="D":
        total=total+50
        RIGHT_Q.append("a4")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a4")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q5()
    a5=input("Enter the a,b,c,d:")
    if a5=="a" or a5=="A":
        total=total+50
        RIGHT_Q.append("a5")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a5")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q6()
    a6=input("Enter the a,b,c,d:")
    if a6=="a" or a6=="A":
        total=total+50
        RIGHT_Q.append("a6")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a6")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q7()
    a7=input("Enter the a,b,c,d:")
    if a7=="a" or a7=="A":
        total=total+50
        RIGHT_Q.append("a7")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a7")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q8()
    a8=input("Enter the a,b,c,d:")
    if a8=="a" or a8=="A":
        total=total+50
        RIGHT_Q.append("a8")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a8")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q9()
    a9=input("Enter the a,b,c,d:")
    if a9=="b" or a9=="B":
        total=total+50
        RIGHT_Q.append("a9")
        print("your score:",total)
    else:
        total=total-20
        WRONG_Q.append("a9")
        print("your score:",total)
    print("--------------------------------------------------------------------------------------")
    q10()
    a10=input("Enter the a,b,c,d:")
    if a10=="d" or a10=="D":
        total=total+50
        RIGHT_Q.append("a10")
    else:
        total=total-20
        WRONG_Q.append("a10")
    print("all question are over")
    print("-----TOTAL SCORE IS:",total)
    if total==500:
        print("-------------------------THE WINNING AMOUNT IS 5 LACS")
    elif 400<=total<500:
        print("-------------------------THE WINNING AMOUNT IS 4 LACS")
    elif 300<=total<400:
        print("-------------------------THE WINNING AMOUNT IS 3 LACS")
    elif 200<=total<300:
        print("-------------------------THE WINNING AMOUNT IS 2 LACS")
    elif total<200:
        print("-------.......CLAP...CLAP....CLAP......----------")

    print("----------------------------------------------------------------------------------------------------------------------")
    

    qtype=int(input("enter 1 is for right question and 2 for wrong question:"))
    print("----------------------------------------------------------------------------------------------------------------------")
    if qtype==1:
        for i in RIGHT_Q:
            if i=="a1":
                q1() 
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a2":
                q2()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a3":
                q3()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a4":
                q4()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a5":
                q5()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a6":
                q6()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a7":
                q7()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a8":
                q8()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a9":
                q9()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a10":
                q10()
                print("----------------------------------------------------------------------------------------------------------------------") 
    elif qtype==2:
        for i in WRONG_Q:
            if i=="a1":
                q1()
                print("----------------------------------------------------------------------------------------------------------------------") 
            elif i=="a2":
                q2()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a3":
                q3()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a4":
                q4()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a5":
                q5()
                print("----------------------------------------------------------------------------------------------------------------------")               
            elif i=="a6":
                q6()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a7":
                q7()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a8":
                q8()
                print("----------------------------------------------------------------------------------------------------------------------") 
            elif i=="a9":
                q9()
                print("----------------------------------------------------------------------------------------------------------------------")
            elif i=="a10":
                q10()
                print("----------------------------------------------------------------------------------------------------------------------") 
            

            
RIGHT_Q=[]
WRONG_Q=[]
N=True
while N:
    N=kbc()
