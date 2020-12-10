
import menu.adminmenu as adminmenu
import reports.prefflight as p_flight
import reports.traveldest as t_dest
import reports.preffclass as p_class
import reports.report as report 



def flight_stats():
    print(" ")
    print('1. PREFERRED FLIGHT ')
    print('2. PREFFERED CLASS')
    print('3. PREFERRED TRAVEL DESTINATION ') #in booking choose flight
    print('4. REVENU REPORT ')
    print('5. EXIT TO MENU < ')    
    option = int(input('enter the respective number : '))
    
    if option==1:
        return p_flight.prefflight_menu()
    elif option==2:
        return p_class.preffclass_menu()
    elif option==3:
        return t_dest.prefdest_menu()
    elif option==4:
        return report.income_report()
    elif option==5:
        return adminmenu.admin_menu()
    else:
        print('the number chosen was incorrect')
        return flight_stats() 
    
    
    