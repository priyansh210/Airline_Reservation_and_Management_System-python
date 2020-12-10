
import menu.login as login

def main():
    print("\n\n #### AIRLINE RESERVATION SYSTEM #### \n")
    print("1. SIGNUP > ")
    print("2 .LOGIN  > ")
    
    option =int(input(":"))
    if option==1:
        return login.signup()
    elif option ==2:
        return login.login()
    else:
        print("><")

main()
                            
         
