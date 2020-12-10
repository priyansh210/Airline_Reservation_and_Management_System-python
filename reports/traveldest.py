
import pandas as pd
import matplotlib.pyplot as plt
import admin.flightstats as flightstats
import sql 
mycursor=sql.mycursor
mydb=sql.mydb

def prefdest_menu():
    print("1 OVERALL : ")
    print("2 MONTHLY : ")
    option = int(input("option : "))
    
    if option==1:
        return tra_dest()
    elif option == 2:
        return tra_dest_monthly()
    else:
        return flightstats.flight_stats()

def tra_dest():
    trav_dest_df = pd.read_sql("select f.T,count(f.T) as count from flight f,booking b where f.code=b.code group by f.T",mydb)
    to_where = list(trav_dest_df.iloc[:,0])
    Coun_list = list(trav_dest_df.iloc[:,1])
    
    plt.bar(to_where,Coun_list)
    plt.xticks(to_where,rotation=90)
    plt.xlabel("DESTINATION")
    plt.ylabel("NO. OF PEOPLE ")
    plt.show()
    return flightstats.flight_stats()

def tra_dest_monthly():
    city=pd.read_sql("SELECT DISTINCT T FROM FLIGHT ",mydb)
    city_list=list(city.iloc[:,0])
    
    month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    total=pd.DataFrame(month,columns=['MONTH'])
    
    for i in city_list :
        df=pd.read_sql("select MONTHNAME(F.DOF) AS MONTH, COUNT(F.T) AS '{}' FROM FLIGHT F , BOOKING B WHERE B.CODE=F.CODE AND F.T='{}' GROUP BY MONTH(F.DOF)".format(i,i),mydb)
        total=pd.merge(total,df,on='MONTH',how='outer').fillna(0)
    
    

    for k in city_list : 
        y=total.loc[:,k]
        plt.plot(month,y,label=k)
    
    plt.xticks(month,rotation=90)
    plt.legend(loc=2,fontsize='x-small')
    plt.ylim(0,100)
    plt.show()
    return flightstats.flight_stats()
    
