
import pandas as pd
import matplotlib.pyplot as plt
import admin.flightstats as flightstats
import sql 
mycursor=sql.mycursor
mydb=sql.mydb


def preffclass_menu():
    print("1 OVERALL : ")
    print("2 MONTHLY : ")
    option = int(input("option : "))
    
    if option==1:
        return pref_class()
    elif option == 2:
        return pref_class_monthly()
    else:
        return flightstats.flight_stats()
    


def pref_class_monthly():
    e_df=pd.read_sql("select MONTHNAME(f.dof) as MONTH ,count(b.seat_no) as ECONOMY from flight f, booking b where seat_no like 'E%' and f.code=b.code group by month(f.dof) order by month(f.dof)",mydb)
    b_df=pd.read_sql("select MONTHNAME(f.dof) as MONTH,count(b.seat_no) as BUSINESS from flight f, booking b where seat_no like 'B%' and f.code=b.code group by month(f.dof) order by month(f.dof)",mydb)
    f_df=pd.read_sql("select MONTHNAME(f.dof) as MONTH,count(b.seat_no) as FIRST from flight f, booking b where seat_no like 'F%' and f.code=b.code group by month(f.dof) order by month(f.dof)",mydb)
    
    month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    
    total=pd.DataFrame(month,columns=['MONTH'])
    
    d=[e_df,b_df,f_df]
    
    for i in d:
        total=pd.merge(total,i,on='MONTH',how='outer').fillna(0)
        
    
       
    economy=list(total.iloc[:,1])
    business=list(total.iloc[:,2])
    first=list(total.iloc[:,3])
    
    plt.plot(month,economy,color='r',label='ECONOMY')
    plt.plot(month,business,color='b',label='BUSINESS')
    plt.plot(month,first,color='g',label='FIRST')
    plt.xlabel("MONTHS")
    plt.ylabel("NUMBER OF SEATS")
    plt.legend()
    plt.xticks(month,rotation=90)
    plt.show()

    return flightstats.flight_stats()


def pref_class():
    pref_class_df= pd.read_sql("select s.class,count(s.class) from seats s,booking b where s.code=b.code and b.seat_no=s.seats group by s.class",mydb)
    class_list=list(pref_class_df.iloc[:,0])
    count_list=list(pref_class_df.iloc[:,1])
    
    plt.bar(class_list,count_list)
    plt.show()
    
    return flightstats.flight_stats()
   

    
