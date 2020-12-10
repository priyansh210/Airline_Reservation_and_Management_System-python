
import pandas as pd 
import menu.login as login
import user.userdetails as userdetails
import menu.usermenu as usermenu
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


#book a flight 

def book_flight(username):
    
    print("\n\n--- WELCOME TO FLIGHT BOOKING --- \n\n")
    
    
    fromw=input("FROM : ")
    tow=input("TO : ")
    date=input("DATE OF TRAVEL (YYYY-MM-DD): \n")
    

    
    d=[fromw,tow,date]  #creating a list of fromwhere, towhere , date of travel 
    
    
    #if the user input any one of the available three criterias -- condition checking 


    df=pd.read_sql("SELECT CODE ,AIRLINE, F AS FROM_ , T AS TO_ ,DOF ,\
                   ECONOMY AS PRICE FROM FLIGHT WHERE F LIKE '%{}%' \
                   AND T LIKE '%{}%' AND DOF LIKE '%{}%' ".format(d[0],d[1],d[2]),mydb)  
    # df is the dataframe of the flights available , checking from sql table 
    
    #check if the dataframe is empty or not 
    if df.empty==True :
        print("THERE ARE NO AVAILABLE FLIGHTS ! ")
        return usermenu.user_menu(username)
        
    #if the flights are availabe then ...
    else:
        print("")
        print(df) #printing the available flights 
        
        #for user to choose the flight 
        code=int(input("ENTER THE CODE OF FLIGHT TO CHOOSE : "))
        
        code_list = list(df.loc[:,'CODE']) #create a list of flight codes in the printed dataframe 
        
     #if the code user has inputed is present in the code list 
        if code in code_list :
            #check if seats for the flight is available 
            print('\n\n',df[df['CODE']==code])
            seat_available=pd.read_sql("SELECT SEATS FROM SEATS WHERE CODE='{}' ".format(code),mydb) 
            #dataframe of seats in the flight 
           
            if seat_available.empty ==True :
                print("NO SEATS AVAILABLE ! ")
                return usermenu.user_menu(username)
            
            else:
                return userdetails.user_details(username,code)
            
        else :#user inputed code doesnt exsist 
            print(" INVALID CODE INPUT ")
            
            print("1 .BOOK A FLIGHT > ")
            print("2 .EXIT          < ")
            menu=int(input("enter option number : "))
            if menu == 1 :
                book_flight(username)
            else:
                login.login()
    
