
import pandas as pd
import menu.usermenu as usermenu
import sql 
mycursor=sql.mycursor
mydb=sql.mydb

def cancel_booking(username):
    user_bookings=pd.read_sql("SELECT * FROM BOOKING WHERE USERNAME='{}' ".format(username),mydb)
    user_bookings=user_bookings.loc[:,['CODE','AIRLINE','SEAT_NO','USERNAME','FIRST_NAME','SECOND_NAME','PRICE']]
    
    if user_bookings.empty == True :
        print("NO BOOKINGS MADE :( " )
        input(">")
        return usermenu.user_menu(username)
    
    print(user_bookings)
    cancel=int(input("ENTER RESPECTIVE NUMBER TO CANCEL BOOKING : "))
    if cancel >= len(user_bookings) :
        print("Please enter valid number ! ")
        input(">")
        return usermenu.user_menu(username)
    else:
        print(user_bookings.loc[cancel,:],'\n')
        seat_no =user_bookings.at[cancel,'SEAT_NO']
        code    =user_bookings.at[cancel,'CODE']
     
        print('1. CONFIRM CANCELLATION OF THE SEAT : ')
        print('2. BACK < \n')
        confirm=int(input('ENTER RESPECTIVE NUMBER : '))
        if confirm==1:
            mycursor.execute("DELETE FROM BOOKING WHERE SEAT_NO='{}' AND CODE='{}' ".format(seat_no,code))
            mydb.commit()
            mycursor.execute("UPDATE SEATS SET BOOKED ='X' WHERE SEATS='{}' AND CODE = '{}' ".format(seat_no,code))
            mydb.commit()
            print("BOOKING CANCELLED \n ")
            return usermenu.user_menu(username)
            
        else:
            return cancel_booking(username)
        

