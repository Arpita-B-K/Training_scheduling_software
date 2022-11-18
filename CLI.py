def sort_fun(sk):
    l=[]
    for ele in sk:
        if(ele != ','):
            l.append(int(ele))
    l.sort()
    sk=""
    for ele in l:
        sk=sk+str(ele)+","
    return sk
    
        

# def create_sch(): # schedule creation
#     print("enter the skill set number seperated by commas")
#     skills=""
#     print("1)python  2)C  3)C++   4)ruby")
#     print("5)algorithms    6)machine-learning    7)datascience  8)Bigdata")
#     print("9)leadership-qualities   10)supportive-member  ")
#     s = input("enter number (to stop enter \'q\'): ")
#     skills = skills+s+","
#     while(s != 'q'):
#             s = input("enter number (to stop enter \'q\'): ")
#             skills = skills+s+","
#     sort_fun(skills)
#     compute_training(skills)
#     print("schedule is been created \n")


def print_sch(user_id):
    sched =  get_schedule(user_id)
    for sch in sched:
        #display in the screen 
        
def print_det_sch():
    pass



def route(choice,user_id):
    if(choice == "1"):
        create_sch(user_id)
    elif(choice =="2"):
        print_sch(user_id)
    elif(choice =="3"):
        print_det_sch(user_id)
    elif(choice == "logout"):
        print("*******************logging out ************************")
        exit()


def emp_dashboard_cli(user_id):
    print("Welcome to "+user_id+"'s schedule keeper")
    print("if you want to get a training, giving a new skill set? please enter 1") 
    print("if you want to get info of your schedules enter 2")
    print("if you want to get a detaile information of your schedules enter 3")
    print("enter \"logout\" to logout")

    choice = input("your choice : ")
    route(choice,user_id)
    while(choice != "logout"):
        print("________________________________________________________")
        choice = input("your choice : ")
        route(choice)
        
def 
    

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
                if(user_type == "emp"):
                    emp_dash_cli(user_id)
                elif(user_type == "hr"):
                    hr_dash_cli(user_id)
                elif(user_type == "admin"):
                    adm_dash_cli(user_id)
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
                reg_dashboard_cli(user_id)
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
            print("***************************************************************************")
            print("************************ invalid login type *******************************")
            print("************************** !terminating! **********************************")
            print("***************************************************************************")
            exit()
        print("invalid input ")
        input_through_cli(n+1)
