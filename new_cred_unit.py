from test_stub import *

def login(n):
        flag = 1
        count=1
        while flag or count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
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
            print("<terminating>")
            exit()
            
            
def reg(n):
        flag = 1
        count = 1
        while flag or count<4:
            user_id = input("please input your user ID :")
            password = input("please input your password :")
            user_type = input("please enter the user type(emp/hr/admin) :")
            if (not(check_presence(user_id))):
                register(user_id,password,user_type)
                flag = 0
                print("valid creds \nSuccesfully Registered")
                user_dashboard_cli(user_id)
            else:
                print("------------------------------------------------")
                print("The user id is begin used \n")
                count += 1 
                
        if(count >=4):
            print("<terminating>")
            exit()

def input_through_cli(n):
    reg_or_login = input("to login enter l and to register enter r : ")
    if (reg_or_login == 'l'):
        login(n)
    elif reg_or_login == 'r':
        reg(n)
    else:
        print("invalid input ")
        if(n >= 4):
            print("<terminating>")
            exit()
        input_through_cli(n+1)
