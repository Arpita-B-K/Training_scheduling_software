
def compute_training(skill_set):
    pass

def get_training(): #function that extracts information from the DBMS of all employees
    pass

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

def create_sch():
    print("enter the skill set number seperated by commas")
    skills=""
    print("1)python  2)C  3)C++   4)ruby")
    print("5)algorithms    6)machine-learning    7)datascience  8)Bigdata")
    print("9)leadership-qualities   10)supportive-member  ")
    s = input("enter number (to stop enter \'q\'): ")
    skills = skills+s+","
    while(s != 'q'):
            s = input("enter number (to stop enter \'q\'): ")
            skills = skills+s+","
    sort_fun(skills)            
    get_training(skills)

def print_sch():
    pass

<<<<<<< HEAD
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
=======
# def get_
>>>>>>> PES1UG20CS646_hitheshdnayak
