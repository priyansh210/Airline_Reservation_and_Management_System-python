
import pandas as pd
import matplotlib.pyplot as plt
import admin.flightstats as flightstats
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


def prefflight_menu():
    print("1 OVERALL : ")
    print("2 MONTHLY : ")
    option = int(input("option : "))
    
    if option==1:
        return pref_flights()
    elif option == 2:
        return pref_flights_monthly()
    else:
        return flightstats.flight_stats()
    

def pref_flights():
    pref_flight_df = pd.read_sql("select airline,count(airline) as count from booking group by airline",mydb)
    airline_list = list(pref_flight_df.iloc[:,0])
    count_list= list(pref_flight_df.iloc[:,1])
    colors = list('rgbkymc')
    
    plt.bar(airline_list,count_list,color=colors) 
    
    plt.xlabel("AIRLINE")
    plt.ylabel("NO. BOOKINGS")
    plt.xticks(airline_list,rotation=90)
    plt.show()
    
    return flightstats.flight_stats()

def pref_flights_monthly():
    airline=pd.read_sql("SELECT DISTINCT AIRLINE FROM FLIGHT ",mydb)
    airline_list=list(airline.iloc[:,0])

    month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    total=pd.DataFrame(month,columns=['MONTH'])

    for i in airline_list :
        df=pd.read_sql("select MONTHNAME(F.DOF) AS MONTH, COUNT(B.AIRLINE) AS '{}' FROM FLIGHT F , BOOKING B WHERE B.CODE=F.CODE AND B.AIRLINE='{}' GROUP BY MONTH(F.DOF)".format(i,i),mydb) #booking per month of individual airlines 
        total=pd.merge(total,df,on='MONTH',how='outer').fillna(0)
    


    for k in airline_list : 
        y=total.loc[:,k]
        plt.plot(month,y,label=k)
    
    plt.xticks(month,rotation=90)
    plt.legend(fontsize='x-small')
    plt.ylim(0,100)
    plt.show()
    
    return flightstats.flight_stats()