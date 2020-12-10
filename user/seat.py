
import pandas as pd 
import user.payment as payment
import sql 
mycursor=sql.mycursor
mydb=sql.mydb

def remove_seat(code,udft):
    alist=list(udft.loc[:,"seat_no"])

    print(alist)
    for i in alist:
        
        mycursor.execute("UPDATE SEATS SET BOOKED ='X' WHERE CODE='{}' AND SEATS ='{}' ".format(code,i))
        mydb.commit()
        
        

def dft_update(udft,total_seats,people):
    if len(udft)==len(total_seats):
        for i in range(len(total_seats)):
            udft.at[i,['seat_no','price']]=total_seats[i]
        print(udft)
        random=input(">")
        if random =='':
            a = udft.loc[:,['price']]
            b = list(a.sum())
            
            print("TOTAL PRICE IS :",b[0])
            print("")
            print("1 .PROCEED TO PAYMENT SECTION > ")
            print("2 .BACK TO SEAT SELECTION < ")
            var=int(input("ENTER RESPECTIVE OPTION NUMBER : "))
            if var==1:
                return payment.payment(b[0],udft)
            else:
                code=udft.at[0,'code']
                remove_seat(code,udft)
                bookseat(udft,code,people)
            
        
def available_seat(code,seat_class):
    df=pd.read_sql("select SEATS FROM SEATS where CODE='{}' and CLASS='{}' and BOOKED LIKE '%X%'".format(code,seat_class),mydb)
    return df 


def bookseat(udft,code,people):
    total_seats=[]
    i=0
    while i < (people):
        print("")
        print("--- SEAT",i+1,"---")
        seat_class=input("ECONOMY/BUSINESS/FIRST : ")
        
        seatdft = available_seat(code,seat_class)
        if seatdft.empty==True:
            print("NO SEATS AVAILABLE :( ")
            continue
        
        
        print(seatdft)
        price=pd.read_sql("select {} from flight where CODE='{}'".format(seat_class,code),mydb)
        price=price.iloc[0,0]
        print("SEAT PRICE : ",price ,"Rs")
        print("")
        seat1=input("ENTER RESPECTIVE NUMBER FOR THE SEAT : ")
        seat=int(seat1)
        
        if seat1=='':
            continue 
        
        seat=int(seat1)
        
        if seat not in list(range(len(seatdft))):
            print("ENTER VALID SEAT")
            input(">")
            continue 
        
        chosen_seat=list(seatdft.loc[seat,:])
        
        print("YOUR SEAT IS : ",chosen_seat[0])
        random=input("PRESS ENTER TO  CONFIRM : ")
        if random=='':
            mycursor.execute("UPDATE SEATS SET BOOKED ='YES' WHERE SEATS ='{}' and CODE='{}' ".format(chosen_seat[0],code))
            
            print(price)
            mydb.commit()
            total_seats.append([chosen_seat[0],price])
            i+=1
        else:
            continue
    return dft_update(udft,total_seats,people)


