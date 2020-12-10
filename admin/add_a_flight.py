
import pandas as pd
import menu.adminmenu as adminmenu
import mysql.connector as mysqlconn


mydb=mysqlconn.connect(host='localhost',user='root',passwd='aeroplaneA1')
mycursor=mydb.cursor()
mycursor.execute(" use airline_test2 ")

def add_flight():
    fd=[]
    
    print("--- ADD A FLIGHT ---")
    print("")
    code=input("ENTER FLIGHT CODE : ")
    code_check=pd.read_sql("SELECT * FROM FLIGHT WHERE CODE = '{}' ".format(code,),mydb)
    if code_check.empty == False:
        print("CODE ALREADY USED ")
        return add_flight()
    fd.append(code)
    
    airline=input("ENTER AIRLINE NAME : ")
    fd.append(airline)
    
    fromw=input("FROM WHERE : ")
    fd.append(fromw)
    
    tow=input("TO WHERE : " )
    fd.append(tow)
    
    departure=input("ENTER DEPARTURE TIME : ")
    fd.append(departure)
    
    arrival=input("ENTER ARRIVAL TIME : ")
    fd.append(arrival)
    
    date=input("ENTER THE DATE OF FLIGHT : ")
    fd.append(date)
    
    economy=float(input("ENTER ECONOMY CLASS SEAT PRICE :"))
    fd.append(economy)
    
    business=float(input("ENTER BUSINESS CLASS SEAT PRICE :"))
    fd.append(business)
    
    first=float(input("ENTER FIRST CLASS SEAT PRICE :"))
    fd.append(first)
    
    for i in fd :
        if i=="":
            print("ONE FIELD IS EMPTY > ERROR > ")
            return add_flight()
    
    mycursor.execute("INSERT INTO FLIGHT VALUES ('{}','{}','{}','{}','{}','{}','{}',{},{},{})".format(code,airline,fromw,tow,departure,arrival,date,economy,business,first))
    mydb.commit()
    print("-------")
    print("FLIGHT ADDED !")
    return add_seats(code,airline)




def add_seats(code,airline):
    print("\n--- ADD SEAT --- ")
    print("")
    e=int(input("ENTER NUMBER OF ECONOMY CLASS SEATS  :"))
    b=int(input("ENTER NUMBER OF BUSINESS CLASS SEATS :"))
    f=int(input("ENTER NUMBER OF FIRST CLASS SEATS    :"))
    print("\n please wait .... adding seats \n")
    for i in range(1,e+1):
        mycursor.execute("INSERT INTO SEATS VALUES ('{}','{}','{}','{}','{}')".format(code,airline,"E"+str(i),"ECONOMY","X"))
        mydb.commit()
    for j in range(1,b+1):
        mycursor.execute("INSERT INTO SEATS VALUES ('{}','{}','{}','{}','{}')".format(code,airline,"B"+str(j),"BUSINESS","X"))
        mydb.commit()
    for k in range(1,f+1):
        mycursor.execute("INSERT INTO SEATS VALUES ('{}','{}','{}','{}','{}')".format(code,airline,"F"+str(k),"FIRST","X"))
        mydb.commit()
        
    print("ALL SEATS ADDED ")
    input('>')
    return adminmenu.admin_menu()