import pandas as pd 
import menu.adminmenu as adminmenu
import sql 

mycursor=sql.mycursor
mydb=sql.mydb


def update_menu():
    print('\n WELCOME TO UPDATE SECTION :')
    print('1. UPDATE SQL DATABASE FROM CSV ')
    print('2. EXPORT SQL DATA TO CSV ')
    print('3. BACK TO MENU')
    option=int(input('ENTER RESPECTIVE OPTION : '))
    if option == 1:
        return update_mysql()
    elif option ==2:
        return update_csv()
    else:
        return adminmenu.admin_menu()
    
    
def update_csv():
    
    user_df=pd.read_sql("Select * from USER ",mydb,index_col='ID')
    user_df.to_csv('USER.csv')
    print('USER CSV UPDATED !')
    
    user_df=pd.read_sql("Select * from BOOKING ",mydb,index_col='CODE')
    user_df.to_csv('BOOKING.csv')
    print('BOOKING CSV UPDATED !')
    
    seats_df=pd.read_sql("Select * from SEATS ",mydb,index_col='CODE')
    seats_df.to_csv('SEATS.csv')
    print('SEATS CSV UPDATED !')
    
    flight_df=pd.read_sql("Select * from FLIGHT ",mydb,index_col='CODE')
    flight_df.to_csv('FLIGHT.csv')
    print('FLIGHT CSV UPDATED !')
    
    return update_menu()

def update_mysql():
    
    for csv in ['USER.csv','BOOKING.csv','SEATS.csv','FLIGHT.csv']  :
        df=pd.read_csv(csv)
        mycursor.execute(str("DELETE FROM "+csv[:-4]))
        print('UPDATING',csv[:-4],'TABLE ...')
        for i in range(len(df)):
            mycursor.execute(str("INSERT INTO " +csv[:-4]+"  VALUES")+str(tuple(df.loc[i,:])))
            mydb.commit()
        print(csv[:-4],'TABLE UPDATED')
    
    print('SQL TABLES UPDATED SUCCESFULLY ')
    
    return update_menu()
            
