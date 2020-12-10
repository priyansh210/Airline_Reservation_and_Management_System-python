
import menu.usermenu as usermenu
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


def make_booking(udft):
    l=len(udft)
    for i in range(l):
        mycursor.execute("INSERT INTO BOOKING VALUES"+str(tuple(udft.loc[i,:])))
        mydb.commit()
    print("YOUR FLIGHT HAS BEEN BOOKED !")
    input("> ")
    
    username = udft.at[0,'username']
    return usermenu.user_menu(username)




def payment(total_amount,udft):
    print("--WELCOME TO THE PAYMENT PORTAL--")
    
    cc_no=int(input("ENTER CREDIT CARD NUMBER : "))
    
    if len(str(cc_no)) != 16:
        print("enter correct credit card no. ")
        payment(total_amount,udft)
    
    udft.loc[:,["creditcard"]]=str(cc_no)
    
    cvv=int(input("ENTER CREDIT CARD CVV (4 max): "))
    if len(str(cvv)) > 4:
        print("enter correct cvv")
        payment(total_amount,udft)
    input("ENTER CREDIT CARD EXPIRY (MM-YYYY): ")  
    
    print(total_amount,"+",(18/100)*total_amount, "(tax) :  Rs is to be deducted ")
    random=input("PRESS ENTER TO AGREE >")
    if random=='': 
        make_booking(udft)
    else:
        payment(total_amount,udft)
