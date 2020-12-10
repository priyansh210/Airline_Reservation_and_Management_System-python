
import admin.add_a_flight as add_a_flight
import admin.cancel_a_flight as cancel_a_flight 
import admin.flightstats as flightstats
import menu.login as login 
import admin.sql_csv_updator as sql_csv_updator


def admin_menu():
    print("")
    print("----WELCOME ADMIN ----")
    print("")
    print("1 . ADD A FLIGHT     >")
    print("2 . CANCEL A FLIGHT  >")
    print("3 . FLIGHT STATS     >")
    print('4 . UPDATE SQL OR CSV ')
    print("5 . EXIT TO LOGIN PAGE... ")
    print(" " )
    
    option=int(input(" : "))
    if option ==1 :
        return add_a_flight.add_flight()
    elif option == 2:
        return cancel_a_flight.cancel_flight()
    elif option == 3:
        return flightstats.flight_stats()
    elif option == 4:
        return sql_csv_updator.update_menu()
    elif option == 5:
        return login.login()
    
    