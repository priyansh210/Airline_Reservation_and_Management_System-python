import mysql.connector as mysqlconn
import pandas as pd
import matplotlib.pyplot as plt
import admin.flightstats as flightstats

mydb=mysqlconn.connect(host='localhost',user='root',passwd='aeroplaneA1')
mycursor=mydb.cursor()
mycursor.execute(" use airline_sys ")

def income_report():
    yearly_repo_df= pd.read_sql("select airline , sum(price) from booking group by airline",mydb)
    airline_list = list(yearly_repo_df.iloc[:,0])
    price_list= list(yearly_repo_df.iloc[:,1])
    
    plt.bar(airline_list,price_list)
    plt.xticks(airline_list,rotation=90)
    plt.xlabel("AIRLINE")
    plt.ylabel("REVENUE")
    plt.show()
    
    return flightstats.flight_stats()


