import pandas as pd
import sys
import menu.usermenu as usermenu
import menu.adminmenu as adminmenu
import sql 
mycursor=sql.mycursor
mydb=sql.mydb

def login():
    
    print("\n\n--- Welcome to login page ---\n\n")
  
    
    username=input("ENTER YOUR USERNAME : ")#enter username 
    password=input("ENTER YOUR PASSWORD : ")#enter password
    
    if (username,password)==("",""):
        sys.exit()
    
    passcheck=pd.read_sql("SELECT PASSWORD from USER where USERNAME = '{}' ".format(username),mydb)
    
    if passcheck.empty==True :
        print("\n Incorrect username or password , please retry \n")
        input(">")
        return login()
    
    elif password==passcheck.iloc[0,0]:  
        if username in ["ADMIN",'admin','Admin']: 
            return adminmenu.admin_menu()
        else:
            return usermenu.user_menu(username)
    else:
        print("password was wrong ! , try again :) ") 
        return login()


def signup():
    username=input("ENTER A USERNAME : ")
    password=input("ENTER A PASSWORD : ")
    first_name=input("ENTER YOUR FIRST NAME : ")
    last_name=input("ENTER YOUR LAST NAME : ")
    email=input("ENTER YOUR EMAIL : ")
    if '' in [username,password,first_name,last_name,email]:
        print('please enter details correctly')
        sys.exit()
        return signup()
    
    else:
        
        mycursor.execute("INSERT INTO USER (USERNAME , PASSWORD , FIRST_NAME , LAST_NAME , EMAIL ) VALUES('{}','{}','{}','{}','{}')".format(username,password,first_name,last_name,email))
        mydb.commit()
        print("SIGNED UP SUCESSFULLY ")
        return login()
    
