
def check_validity(emp_id,password,type):
    if(emp_id == "bayer" and password == "abcd1234" and type == "emp"): #tells that this tupel is valid and others are invalid
        return True
    return False

def check_presence(emp_id):
    
    if((emp_id == "tom" ) or(emp_id == "suresh") or(emp_id == "bunty" )): # tells that the database already contains these users and currently cannot take this.
        return True
    return False

def user_dashboard_cli(emp_id):
    print("The training section has beed opened to the user "+emp_id ) # this is printing the user corresponding to the dashboard.
    v=""
    while(v != "logout"):
        v= input("please enter the details(to leave interface enter \"logout\")") # emulates the future code inside the dashboard.
    return