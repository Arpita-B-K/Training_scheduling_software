First we start by designing a database

DATABASE:
credentials(user_id,name,password,user_type)
#user_logs(user_id,password,login_date,login_time,logout_time)
job(role_id,role_name,skills_required)
employee(emp_id,name,role_id,skillset)
training(skill,training,test,parscore)  
schedule(emp_id,training,start_date,end_date,test,score)

DATABASE CONSTRAINTS:
credentials - pk(user_id)
job - pk(role_id)
employee - pk(emp_id) fk(role_id) references job(role_id)
training - pk(skill)
schedule - pk(emp_id,training)

ACCESS:
We have 2 users - Employee and HR

then we grant differnt permissions to each
1.Employee
-> update on employee   # grant update on employee for employee
-> select on schedule,employee,job  # grant select on job for employee

2.HR
-> update on job,training   
-> select on schedule,employee,job,training
-> delete on job,training   # grant delete on training for HR

################## Programming part #################

1. Identifying training needs
Compare the job(skills_required) and employee(skillset)
    skills_need_to_be_trained = job(skills_required) - employee(skillset)

2.for each skill in skills_need_to_be_trained:
    add the corresponding training and test to schedule table

3.test is provided with user-interface
    score of test is updated to database
    if score>parscore:
        corresponding skill is updated to employee skillset

################# User-Interface ####################

1.Login_page
    features-login form

2.Employee_page
    features-view schedule

3.HR_page
    features-update training_needs






