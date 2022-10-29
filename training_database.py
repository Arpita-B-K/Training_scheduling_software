import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    # database="Training_Software"   #to be uncommented after creating the database
)

mycursor=mydb.cursor()  #initialise the cursor for communication

# Creating the database
q1='create database training_software'
mycursor.execute(q1)

#Checking whether the data base is created or not
# q2='show databases'
# mycursor.execute(q2)

# for db in mycursor:
#     print(db)

#NOTE: after creating the database add the database to cursor 

#Creating a table
# user id (primary key),password,name,user type(admin,hr,employee(patron))
q3='create table Credentials(user_id varchar(10),password varchar(10) not null,user_type enum(admin,hr,employee) not null,primary key(user_id))'
mycursor.execute(q3)

# cols: emplyee id,the required training to be provided to the emmployees,start date , end date ,test link for attending.
q4='create table schedule(Employee_id varchar(10),training_name varchar(20),start_date date,end_date date,test_link varchar(200),primary key(employee_id))'
mycursor.execute(q4)

#cols:user id,name,logdate,login time, logout time
q5='create table user_logs(user_id varchar(10),name varchar(30),logdate date,login_time timestamp, logout_time timestamp,primary key(user_id))'
mycursor.execute(q5)

# skillset required(comma seperated),the required training to be provided to the emmployees.
q6='create table training(employee_id varchar(10),role_id varchar(10),role_name varchar(30),skillset_required tinytext,training_required tinytext,primary key(employee_id,role_id))'
mycursor.execute(q6)

#closing the connection
mydb.close()




