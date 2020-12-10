
import user.book_a_flight as book_a_flight
import user.cancelbooking as cancelbooking
import menu.login as login



def user_menu(username):
    
    print("")
    print("----WELCOME ",username.upper()," ----")
    print("")
    print("1 . BOOK A FLIGHT ")
    print("2 . CANCEL A BOOKING ")
    print("3 . EXIT TO LOGIN PAGE ..")
    print(" " )
    
    #input value for menu 
    menu1=int(input("Enter the respective number : "))
    
    if menu1 == 1:
        return book_a_flight.book_flight(username)
    elif menu1 == 2:
        return cancelbooking.cancel_booking(username)
    elif menu1 == 3 :
        return login.login()
        
