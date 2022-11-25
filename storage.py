    
def add_cred(user_id,password,type):
    #adds the tuple to credentials table
    pass


def check_validity(user_id,password,test,parsecore):
    #if the tupe is present in the table credentials returns True otherwise False
    pass


def HRs_data_modify(skills,training,mode):
    #mode stores the code
    # 1 - insert tupel
    # 2 - delete tupel
    # 3 - update tupel
    # update tupe returns true all the time after the update
    # for 1 if the skill attribute is already present return False, return True if not present and added newly to table
    # for 2 return false if not present and handle the event properly ,return True if succesfull deletion
    pass

def get_training(skills):
    #returns training corresponding to the skills mentioned from the training table
    pass

def schedule(emp_id,training,startdate,enddate,testlink,score):
    #inserts the tuple in the schedule table
    pass

def get_schedule(emp_id):
    pass

def check_presence(emp_id):
    #same as check_validity but here it checks only if the user id is present in the table
    pass