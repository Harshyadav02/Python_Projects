import time
import datetime
import mysql.connector as c
con = c.connect(host =" localhost" ,user ="root",passwd="",database="harshdb")
cur =con.cursor()

print(" WELCOME TO LAXMI CHEAT FUNDS ")
print()

first_Name  = ''
Last_Name   = ''
cardNum     = ''
pin  	    = ''
balance     = ''
withdraw    = ''
Deposit     = ''


def login():
    
        info = (input("Enter your Card_Number "))
        print()
        print("Please wait ...")
        time.sleep(2)
        

        cur = con.cursor()
        cur.execute("""select * from customer_details where cardNum ='%s'""" %(info))

        row =cur.fetchone()
        if cur.rowcount ==1:
             print()
             passw = int(input("Enter your password "))
             cur.execute(''' select * from customer_details where pin = '%s' '''%(passw))
             row =cur.fetchone()
             cur.execute(''' select first_name ,Last_name from customer_details where pin = '%s' '''%(passw))
             name =cur.fetchone()
             
             if cur.rowcount == 1:
                print("Login Succecful Welcome " ,name)
             else:
                print()
                print("Password Invalid Try again")
                return
        

             def withdraw():
                        
                        amount = int(input("Enter the amount you wanna withdraw "))
                        cur.execute(''' select balance from customer_details where cardNum ='%s' '''%(info))  
                        myres =cur.fetchone()
                        x =list(myres)
                        bal = 0
                        for i in x:
                               db = int(i)
                               bal = db
                        if(bal >= amount):
                                cur.execute(''' select balance from customer_details where cardNum = '%s' '''%(info))
                                col = cur.fetchone()
                                x =list(col)
                                for i in x:
                                        z =(int(i))
                                        c = z- amount
                                print()
                                print(datetime.datetime.now())
                                cur.execute(" UPDATE customer_details SET balance = '%s' WHERE cardNum ='%s' "%(c,info))
                                cur.execute(" UPDATE customer_details SET Withdraw = '%s' WHERE cardNum ='%s' "%(amount,info))
                                con.commit()
                                print("Amount Debited :",amount)
                        else:
                                 print("Insufficent Balance ")
                
             def deposit():
                        amount = int(input("Enter the amount you wanna deposit "))

                        cur.execute(''' select balance from customer_details where pin = '%s' '''%(passw))
                        col = cur.fetchone()
                        x =list(col)
                        c = 0
                        c1 = amount
                        for i in x:
                                z =(int(i))
                                c = z+ amount
                        print()
                        print(datetime.datetime.now())
                        cur.execute(''' update customer_details SET balance = '%s' where cardNum ='%s' '''%(c,info))
                        cur.execute(''' update customer_details SET Deposit = '%s' where cardNum ='%s' '''%(c1,info))
                        print("Amount Deposited :",c1)
                        con.commit()
                

             def pin_update():
                        passw = int(input(" Enter your new Password "))

                        cur.execute("select pin from customer_details where cardNum = '%s' " %(info))

                        col =cur.fetchone()
                        cur.execute(''' update customer_details SET pin = '%s' where cardNum ='%s' '''%(passw,info))
                        con.commit()
             def Bal_query():
                      cur.execute(''' select balance from customer_details where cardNum ='%s' '''%(info))  
                      myres =cur.fetchone()
                      x =list(myres)
                      for i in x:
                         bal = (int(i))
                      print("Your Balance is :",bal)
             
             def mini_statment():
                print()
                print(datetime.datetime.now())
                print()
                print("Transaction :  MiniStatment")
                print()
                print("---------------------")
                print("First_Name : ",)
                print()
                print("Last_Name : ",)
                print()
                print("Card Number : ",)
                print()
                print("Balance : ",)
                print()
               
                print("---------------------")
                print()

                
                
             while True:
                        print()
                        print("press choose an valid option : ")
                        print()
                        print("""
                        1  Deposit
                        2  withdraw
                        3  Balance_Check
                        4  update_pin
                        5  exit
                        """)
                        try:
                           option=int(input("enter your choice  "))
                           print()
                        except:
                           print("please enter valid option  ")
                        if option == 1:
                                deposit()
                        elif option == 2:
                                withdraw()
                        elif option == 3:
                                Bal_query()
                        elif option == 4:
                                pin_update()
                        elif option == 5:
                                break
        else:
                print("Account does not exist ")
                print()
                print(" Please Vist Your Bank ")
login()
print()
print("HAVE A NICE DAY SIR/MADAM ")
                              
        
               
                 
 





