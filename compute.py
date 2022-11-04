def check_presence(id, pas, type):
    # dbms part this will check if the tupel is presnt in the database or not
    pass

def user_dashboard_cli(user_id):
    pass

def input_through_cli(n):
    reg_or_login = input("to login enter l and to register enter r")
    if (reg_or_login == 'l'):
        flag = 1
        count=1
        while flag and count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if (check_presence(user_id, password, user_type)):
                flag = 0
                user_dashboard_cli(user_id)
            else:
                count += 1
                
        if(count >=4):
            print("***************************************************************************")
            print("************************* wrong credentials *******************************")
            print("************************** !terminating! **********************************")
            exit()
            
    elif reg_or_login == 'r':
        pass
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
