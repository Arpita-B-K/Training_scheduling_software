

def create_sch():
    pass

def print_sch():
    pass

def print_det_sch():
    pass



def route(choice):
    if(choice == "1"):
        create_sch()
    elif(choice =="2"):
        print_sch()
    elif(choice =="3"):
        print_det_sch()
    elif(choice == "logout"):
        print("*******************logging out ************************")
        exit()
        



def user_dashboard_cli(user_id):
    print("Welcome to "+user_id+"'s schedule keeper")
    print("if you want to get a training, giving a new skill set? please enter 1") 
    print("if you want to get info of your schedules enter 2")
    print("if you want to get a detaile information of your schedules enter 3")
    print("enter \"logout\" to logout")
    
    choice = input("your choice : ")
    route(choice)
    while(choice != "logout"):
        print("________________________________________________________")
        choice = input("your choice : ")
        route(choice)
        
    

def input_through_cli(n):
    reg_or_login = input("to login enter l and to register enter r")
    if (reg_or_login == 'l'):
        flag = 1
        count=1
        while flag and count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if (check_validity(user_id, password, user_type)):
                flag = 0
                user_dashboard_cli(user_id)
            else:
                print("------------------------------------------------")
                print("This inputs are wrong so please input again\n")
                count += 1
                
        if(count >=4):
            print("***************************************************************************")
            print("************************* wrong credentials *******************************")
            print("************************** !terminating! **********************************")
            print("***************************************************************************")
            exit()
            
    elif reg_or_login == 'r':
        flag = 1
        count = 1
        while flag and count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if (not(check_presence(user_id, password, user_type))):
                flag = 0
                print("-------------------------------------------------------------")
                print("the details are valid and you can use this cred further.")
                print("Succesfully Registered")
                print("-------------------------------------------------------------")
                user_dashboard_cli(user_id)
            else:
                print("------------------------------------------------")
                print("The user id is begin used \n")
                count += 1
                
        if(count >=4):
            print("***************************************************************************")
            print("************************* invalid credentials *****************************")
            print("************************** !terminating! **********************************")
            print("***************************************************************************")
            exit()
    else:
        if(n >= 4):
            exit()
        print("invalid input ")
        input_through_cli(n+1)


def input_choice():
    cli_types = ["CLI", "Cli", "cli", "cLi", "clI", "CLi", "ClI", "cLI"]
    gui_types = ["GUI", "Gui", "gui", "gUi", "guI", "GUi", "GuI", "gUI"]
    flag = 1
    while flag:
        choice = input("do you want to input through CLI or GUI ?:")
        print("\n")
        if choice in gui_types:
            flag = 0
            # input_through_gui()
        elif choice in cli_types:
            flag = 0
            input_through_cli(1)
        else:
            print("invalid Input  !! ")
