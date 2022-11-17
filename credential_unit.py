from test_stub import *

def input_through_cli(n):
    reg_or_login = input("to login enter l and to register enter r : ")
    if (reg_or_login == 'l'):
        flag = 1
        count=1
        while flag or count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if(user_type not in {"emp","hr","admin"}):
                print("------------------------------------------------")
                print("This inputs are wrong so please input again\n")
                count += 1
            else:
                if (check_validity(user_id, password, user_type)):
                    flag = 0
                    if(user_type == "emp"):
                        emp_dash_cli(user_id)
                    elif(user_type == "hr"):
                        hr_dash_cli(user_id)
                    elif(user_type == "admin"):
                        adm_dash_cli(user_id)
                else:
                    print("------------------------------------------------")
                    print("This inputs are wrong \n")
                    count += 1
                
        if(count >= 4):
            print("***************************************************************************")
            print("************************* wrong credentials *******************************")
            print("************************** !terminating! **********************************")
            print("***************************************************************************")
            exit()
            
    elif reg_or_login == 'r':
        flag = 1
        count = 1
        while flag or count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if(user_type not in {"emp","hr","admin"}):
                print("------------------------------------------------")
                print("This inputs are wrong so please input again\n")
                count += 1
            else:
                if (not(check_presence(user_id))):
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
        print("invalid input ")
        if(n >= 4):
            print("***************************************************************************")
            print("************************ invalid login type *******************************")
            print("************************** !terminating! **********************************")
            print("***************************************************************************")
            exit()
        input_through_cli(n+1)


if __name__=="__main__":
    input_through_cli(1)
