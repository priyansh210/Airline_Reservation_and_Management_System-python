import mysql.connector as mysqlconn


mydb=mysqlconn.connect(host='localhost',user='root',passwd='')
mycursor=mydb.cursor()
mycursor.execute(" use airline_sys ")