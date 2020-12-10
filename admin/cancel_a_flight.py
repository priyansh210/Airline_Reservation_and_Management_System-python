
import pandas as pd
import  menu.adminmenu as adminmenu
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


def cancel_flight():
    df=pd.read_sql("SELECT CODE ,AIRLINE, F AS FROM_ , T AS TO_ ,DOF  FROM FLIGHT",mydb)
    print(df)
    
    code = int(input("ENTER THE CODE OF FLIGHT YOU WANT TO DELETE : "))
    code_list=list(df.loc[:,'CODE'])
    if code not in code_list:
        print("ENTER A VALID CODE ! ")
        return adminmenu.admin_menu()
    
    print("YOU WANT TO DELETE FLIGHT CODE :",code)
    print(pd.read_sql("SELECT CODE ,AIRLINE, F AS FROM_ , T AS TO_ ,DOF  FROM FLIGHT WHERE CODE = {} ".format(code),mydb))
    x=input("\n Proceed ? >")
    if x in ['No','no','N','n']:
        return cancel_flight()
    else:
        mycursor.execute("DELETE FROM FLIGHT WHERE CODE = '{}' ".format(code))
        mycursor.execute("DELETE FROM SEATS WHERE CODE = '{}' ".format(code))
        mycursor.execute("DELETE FROM BOOKING WHERE CODE = '{}' ".format(code))
        mydb.commit()
        
        print("\n FLIGHT CANCELLED !")
        return adminmenu.admin_menu()
        