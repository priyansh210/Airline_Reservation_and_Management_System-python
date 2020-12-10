
import pandas as pd 
import user.seat as seat  
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


#user details 
        
def user_details(username,code):
    people=int(input("ENTER THE NUMBER OF PEOPLE : "))
 
    
    #make a empty dataframe of passenger details 
    udft=pd.DataFrame(columns=["code","seat_no",'username','firstname','lastname','gender',
                               'age','nationality','creditcard',"airline","price"])
    
    airline_dft=pd.read_sql("select AIRLINE from FLIGHT WHERE CODE ='{}' ".format(code,),mydb)
    airline=airline_dft.iat[0,0]
    #adult data entry 
    i=0
    while i < people:
        random=input("___PRESS ENTER FOR ENTRY ___")
        print("")
        print("______DETAILS OF PERSONS ",i+1,"______")
        print("")
        
        firstname=input("ENTER FIRST NAME : ")
        firstname=firstname.upper()
        
        lastname=input("ENTER LAST NAME : ")
        lastname=lastname.upper()
        
        gender=input("ENTER YOUR GENDER : ")
        gender=gender.title()
        
        age=int(input("ENTER YOUR AGE : "))
        
        nationality=input("ENTER YOUR NATIONALITY : ")
        nationality=nationality.title()
        print("")
        udft.loc[i,["code","airline",'username','firstname','lastname','gender','age',
                    'nationality']]=[code,airline,username,firstname,lastname,gender,age,nationality]
        i+=1

        
        #PRINT DATAFRAME 
    print(udft.loc[:,["code","airline",'username','firstname','lastname','gender','age','nationality']])
    
    random=input("PRESS ENTER TO CONFIRM DETAILS ")
    if random=='':
        return seat.bookseat(udft,code,people)
    else:
        udft=udft.iloc[0:0]
        user_details(username,code)
    

        
        
    
    
    
    
    
    
    
    