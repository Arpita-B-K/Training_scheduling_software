
from tkinter import *
from tkinter import messagebox
import mysql.connector
import webbrowser
import hashlib
mydb=mysql.connector.connect(host="localhost", user="root", 
	database="Training_Software"
	)
mycursor=mydb.cursor(buffered=True)
  
#table credential
#create table Credentials(user_id int auto_increment,name varchar(20) not null, username varchar(20) not null unique, 
#password varchar(50) not null, user_type enum('admin', 'hr', 'employee') not null, primary key(user_id));


def usertype(user_type):
	if user_type==1:
		return "employee"
	elif user_type==2:
		return "hr"
	elif user_type==3:
		return "admin"			


#CLASS WINDOW
class window(Tk):
	def __init__(self):
		Tk.__init__(self)
		Label(self, text="TRAINING SCHEDULING SOFTWARE", font='Helvetica 18 bold', bg="light green", fg="white").pack()
		Label(self, text="").pack()
		self.geometry="500x500"

		Label(self, text="").pack()
		#initialize frame to none
		self._frame = None
		#default frame switch to sign in page
		self.switch_frame(signin_page)

	def switch_frame(self, frame_class):
		"""Destroys current frame and replaces it with a new one."""
		#creates a new frame of a frame_class passed as parameter
		new_frame = frame_class(self)
		#checks if a frame is already displaying, if yes destroys it
		if self._frame is not None:
			self._frame.destroy()
		#displays the new frame
		self._frame = new_frame
		self._frame.pack()



#CLASS SINGUP PAGE
class signup_page(LabelFrame):
	def __init__(self, master):
		#creating a frame inside main window
		LabelFrame.__init__(self, master)
		
		#display label text
		Label(self, text="Please enter your Signup details", font='Helvetica 12 bold', bg="light blue").grid(row=0)
		#empty space
		Label(self, text="").grid(row=1)


		#label and entry box for USERTYPE
		Label(self, text="USERTYPE", font='Helvetica 12 bold').grid(row=2)
		self._usertype_signup_entry = IntVar()
		usertypes = [("Employee", 1),
					("HR", 2),
					("Admin", 3)]
		for usrty, val in usertypes:
			Radiobutton(self, text=usrty, font='Helvetica 10 bold', activebackground="light grey", indicatoron = 0, width = 10, padx = 5 ,variable=self._usertype_signup_entry, value=val).grid(row=val+2)	

		
		#empty space
		Label(self, text="").grid(row=6)

		#label and entry box for USERNAME
		Label(self, text="USERNAME", font='Helvetica 12 bold').grid(row=7)
		self._username_signup_entry = Entry(self, textvariable="username_signup", bg="light grey")
		self._username_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._username_signup_entry.grid(row=8)
		#empty space
		Label(self, text="").grid(row=9)

		#label and entry box for PASSWORD
		Label(self, text="PASSWORD", font='Helvetica 12 bold').grid(row=10)
		self._password_signup_entry = Entry(self, textvariable="password_signup", show= '*', bg="light grey")
		self._password_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._password_signup_entry.grid(row=11)

		#self.mandatory_entry(self.password_signup_entry)
		#empty space
		Label(self, text="").grid(row=12)

		#Signup button
		Button(self, text="SIGNUP", bg="blue", fg="white",borderwidth=4, width=10, font='helvetica 10 bold',
                       relief=GROOVE, highlightthickness=1, highlightcolor= "blue",command = lambda:[self.mandatory_entry(master)]).grid(row=13)

		Label(self, text="").grid(row=14)
		Button(self, text="Already have account?Signin", font= ('Helvetica 8 underline'),fg="purple", highlightthickness=1, highlightcolor= "blue", command= lambda: [self.reset(),master.switch_frame(signin_page)]).grid(row=15)

	def add_credentials(self,entry_list, master):
		#search for same username in the database
		#if same username is found, display "user with this username already exists, try other name or if u already have
		# an account try signing in" pop message box asking yes or no if he wants to go to signin page
		#if no stays in signup page
		#if yes continues in mandatory_entry function

		#if no same username is found, insert into table 'credentials'
		entry_list_val=[]
		for i in entry_list:
			entry_list_val.append(i.get())
		q1="SELECT * FROM credentials WHERE name=%s"
	
		mycursor.execute(q1, (entry_list_val[0],))
		ans1=mycursor.fetchall()
		if ans1==[]:
			hashed_password=self.encrypt_password(entry_list_val[1])

			q2='insert into credentials(name, password, user_type) values(%s, %s, %s)'
			val2=(entry_list_val[0], hashed_password, usertype(entry_list_val[2]))
			mycursor.execute(q2, val2)
			mydb.commit()
			print(mycursor.rowcount, "record inserted.")
			if mycursor.rowcount==1:
				self.reset()
				master.switch_frame(signin_page)
		else:
			answer=messagebox.askyesno("useralreadyexists","ERROR!\nUser with this username already exists\nTry with another username\nDO YOU ALREADY HAVE AN ACCOUNT?")
			if answer:
				master.switch_frame(signin_page)

	
	def mandatory_entry(self, master):
    	#appending all entry widgets to a list	
		entry_list = []
		entry_list.append(self._username_signup_entry)
		entry_list.append(self._password_signup_entry)
		entry_list.append(self._usertype_signup_entry)
		count = 0
		#checking entry field,countinf the number of filled entry boxes 
		for i in entry_list:
			if i.get():
				count+=1
		#IF all entry box are entered 
		# THEN check IF the user with same credential already not exists 
		# THEN add credentials to database and reset all entry boxes and switch frame to signin_page
		if count==3:
			self.add_credentials(entry_list, master)
		else:
			messagebox.showerror("showerrormandatoryfields", "Information\nPlease enter the mandatory fields")
	def encrypt_password(self, password):
		password = password.encode("utf-8")
		encoded_text = hashlib.md5(password).hexdigest()		
		return encoded_text	
			
	def reset(self):
		self._username_signup_entry.delete(0, END)
		self._password_signup_entry.delete(0, END)
		self._usertype_signup_entry.set(None)	


emp_id = ""		


#CLASS SIGNIN PAGE
class signin_page(LabelFrame):
	def __init__(self, master):
		#creating a frame inside main window
		LabelFrame.__init__(self, master)
		
		#display label text
		Label(self, text="Please enter login details", font='Helvetica 12 bold', bg="light blue").grid(row=0)
		#empty space
		Label(self, text="").grid(row=1)
		
		#USERNAME label display
		Label(self, text="USERNAME", font='Helvetica 12 bold').grid(row=2)
		#box for taking entry from user for username
		self._username_login_entry = Entry(self, textvariable="username")
		self._username_login_entry.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self._username_login_entry.grid(row=3)
		#empty space
		Label(self, text="").grid(row=4)
		
		#PASSWORD label display
		Label(self, text="PASSWORD", font='Helvetica 12 bold').grid(row=5)
		#box for taking entry from user for password
		self._password__login_entry = Entry(self, textvariable="password", show= '*')
		self._password__login_entry.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self._password__login_entry.grid(row=6)
		#empty space
		Label(self, text="").grid(row=7)
		
		self._usertype_login_entry = IntVar()
		#checkbuttons for user type
		employee = Radiobutton(self, padx = 20, text="Employee", font='Helvetica 10 bold',variable=self._usertype_login_entry , value=1)
		employee.grid(row=8, sticky=W)
		hr = Radiobutton(self, padx = 20, text="HR", font='Helvetica 10 bold', variable=self._usertype_login_entry, value=2)
		hr.grid(row=9, sticky=W)
		admin = Radiobutton(self, padx = 20, text="Admin", font='Helvetica 10 bold', variable=self._usertype_login_entry, value=3)
		admin.grid(row=10, sticky=W)
		
		#empty space
		Label(self, text="").grid(row=11)
		#lOGIN button
		Button(self, text="Login",width=10, height=1, bg="green", fg="white", borderwidth=4,font='Helvetica 10 bold', 
                       relief=GROOVE, command=lambda: self.mandatory_entry(master)).grid(row=12)
		#empty space
		Label(self, text="").grid(row=13)
		
		#goto signup page
		Button(self, text="Don't have account?Signup",font= ('Helvetica 8 underline'),fg="blue", highlightthickness=1, highlightcolor= "blue", command= lambda: [master.switch_frame(signup_page)]).grid(row=14)

		

	def check_cred(self, entry_list, master):
    	#check for same username in the database
		# if found check for password  Then if both are correct switch to main page of that usertype else display message invalid credentials
		entry_list_val=[]
		for i in entry_list:
			entry_list_val.append(i.get())
			print(i.get())
		entry_list_val[1]=self.encrypt_password(entry_list_val[1])
		entry_list_val[2]=usertype(entry_list_val[2])
		q1='SELECT * FROM credentials WHERE name=%s'
		mycursor.execute(q1, (entry_list_val[0],))
		myresult = mycursor.fetchone()
		myresult=list(myresult)
		if myresult!=[]:	
			emp_id = myresult[0]
			del myresult[0]
			if myresult==entry_list_val:
				self.reset()
				if myresult[-1]=='employee':
					master.switch_frame(main_page_emp)
				elif myresult[-1]=='hr':
					master.switch_frame(main_page_hr)
				elif myresult[-1]=='admin':
					master.switch_frame(main_page_admin)	
			else:
				messagebox.showerror("wrongpassword", "ERROR!\nPlease enter correct PASSWORD")
		else:
			messagebox.showerror("wrongusername", "ERROR!\nPlease enter correct USERNAME")		

	def mandatory_entry(self, master):

		entry_list = []
		entry_list.append(self._username_login_entry)
		entry_list.append(self._password__login_entry)
		entry_list.append(self._usertype_login_entry)
		count = 0
		for i in entry_list:
			if i.get():
				
				count+=1
		#IF all entry fields are entered THEN check credentials with credentials in database	
		# and IF credentials are matched THEN reset the entry fields and switch frame to main_page
		
		if count==3:
			utype = self._usertype_login_entry.get()
			emp_id = self.check_cred(entry_list, master)
						
		else:
			messagebox.showerror("showerrormandatoryfields", "Error\nPlease fill the mandatory fields")	
	def encrypt_password(self, password):
		password = password.encode("utf-8")	
		encoded_text = hashlib.md5(password).hexdigest()		
		return encoded_text
	def reset(self):		
		self._username_login_entry.delete(0, END)
		self._usertype_login_entry.set(None)
		self._password__login_entry.delete(0, END)				

#CLASS MAIN PAGE OF EMPLOYEE
class main_page_emp(LabelFrame):
	def __init__(self, master):
    	#creating  a new frame
		LabelFrame.__init__(self, master)
		welcome = Label(self, text="Welcome to training scheduling software!!", relief=RAISED,font='Helvetica 9 bold', bg="light pink")
		welcome.grid(row=1,column=1)
		self.after(3000, welcome.destroy)
		#display TASK LIST text
		Label(self, text="Tasks list", width=10, font=('Helvetica 14 underline')).grid(row=2, column=1)
		#empty space
		Label(self, text="").grid(row=3, column=1)	
		#buttons lists of task list	
		self.task_list = []
		self.emp_id = emp_id

		#USER INFO
		#empty space
		Label(self, text="").grid(row=2, column=7)
		
		#NAME
		Label(self, text="Name:", font=('Helvetica 10 bold')).grid(row=3, column=7)
		#text box for name
		self.Tname = Text(self, height = 1, width = 10, relief=GROOVE)
		self.Tname.grid(row=3, column=8)
		
		#STARTDATE
		Label(self, text="Startdate:", font=('Helvetica 10 bold')).grid(row=4, column=7)
		#textbox for startdate
		self.Tsd = Text(self, height = 1, width = 10, relief=GROOVE)
		self.Tsd.grid(row=4, column=8)
		
		#DUEDATE
		Label(self, text="Duedate:", font=('Helvetica 10 bold')).grid(row=5, column=7)
		#textbox for duedate
		self.Tdd = Text(self, height = 1, width = 10, relief=GROOVE)
		self.Tdd.grid(row=5, column=8)
		
		#INFO
		#Label(self, text="Info:", font=('Helvetica 10 bold')).grid(row=6, column=7)
		#textbox for info
		#self.Tif = Text(self, height = 1, width = 10, relief=GROOVE)
		#self.Tif.grid(row=6, column=8)
		
		#empty space
		Label(self, text="").grid(row=7, column=8)
		#button for take test function
		self.take_test = Button(self, text="Take Test", width=10, bg="green", fg="black", borderwidth=4,
                       relief=GROOVE, command=lambda:[self.take_test(self.take_test)], font=('Helvetica 10 bold'))
		#take_test.grid(row=8, column=8)
		self.take_test.visible=False

		#button for logging out 
		Button(self, text="Logout", bg="blue", fg="white", borderwidth=3,
                       relief=GROOVE, command=lambda: master.switch_frame(signin_page), font=('Helvetica 8 bold')).grid(row=1, column=8)

	def task_append(self):
		
		#search for 'emp_id' in 'schedule' table and get 'training names' and append to 'task_list'
		

		for i in range(len(self.task_list)):
			task_button = Button(self, text=self.task_list[i], width=10, font=('Helvetica 10 bold'), command=self.fill_text(task_button), bg="green", fg="white").grid(row=4+i, column=1)
    		
	def fill_text(self, task_button):
		task_name = task_button['text']
    	#retrieve the emp name and startdate and end date using emp_id and task_name
		#instance of record
		record = ["emp_001","train1", "12/12/2022","12/01/2023",""]	
		#inseting them into text feild
		self.Tname.insert(END, record[0])
		self.Tsd.insert(END, record[2])
		self.Tdd.insert(END, record[3])
		#self.Tif.insert(END, info)	
		self.take_test.visible=True

	def take_test(self):
    	#retrieve the test link from database for that emp_id and task
		record="link"
		webbrowser.open(record)



#CLASS MAIN PAGE OF HR
class main_page_hr(LabelFrame):
	def __init__(self, master):
		LabelFrame.__init__(self, master)

		welcome = Label(self, text="Welcome to training scheduling software!!", relief=RAISED, font='Helvetica 9 bold', bg="light pink")
		welcome.grid(row=0)
		self.after(3000, welcome.destroy)
		#taking input of employee_id
		Label(self, text="Employee_id of employee", font='Helvetica 12 bold').grid(row=1)
		self.employee_id = Entry(self, textvariable="employee_id")
		self.employee_id.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self.employee_id.grid(row=2)
		Label(self, text="").grid(row=3)

		Label(self, text="Role_id of employee", font='Helvetica 12 bold').grid(row=4)
		self.role_id = Entry(self, textvariable="role_id")
		self.role_id.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self.role_id.grid(row=5)
		Label(self, text="").grid(row=6)

		Label(self, text="Skills required", font='Helvetica 12 bold').grid(row=7)
		Label(self, text="(enter the skills name separated by comma)", font='Helvetica 8').grid(row=8)
		self.skills_set = Entry(self, textvariable="skills_set")
		self.skills_set.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self.skills_set.grid(row=9, padx=10,
               pady=10,
               ipadx=20,
               ipady=15)
		Label(self, text="").grid(row=10)

		Label(self, text="Trainings required", font='Helvetica 12 bold').grid(row=11)
		Label(self, text="(enter the trainings name separated by comma)", font='Helvetica 8').grid(row=12)
		self.train_set = Entry(self, textvariable="train_set")
		self.train_set.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self.train_set.grid(row=13, padx=10,
               pady=10,
               ipadx=20,
               ipady=15)

		Button(self, text="SUBMIT", bg="blue", fg="white", borderwidth=4,
                       relief=GROOVE, font='Helvetica 10 bold', command= self.mandatory_entry()).grid(row=14)		   
		Button(self, text="Logout",  font='Helvetic 10 bold', bg="light blue", fg="white", command=lambda:[master.switch_frame(signin_page)]).grid(row=0, column=2)

	def mandatory_entry(self):
		entry_list=[]
		entry_list.append(self.employee_id)
		entry_list.append(self.role_id)
		entry_list.append(self.skills_set)
		entry_list.append(self.train_set)
		count = 0
		for i in entry_list:
			if i.get():
				count+=1
		if count==4:
    		#add to database 
			#if correctly added to database display a correct message 
			messagebox.showinfo("correctinsertionintodatabase", "All entries have been added \nto database correctly")
		else:
			messagebox.showerror("notenteredmandatoryfields", "ERROR!\nPlease enter all the mandatory fields")	


# CLASS MAIN PAGE ADMIN    				
class main_page_admin(LabelFrame):
	def __init__(self, master):
		LabelFrame.__init__(self, master)
		welcome = Label(self, text="Welcome to training scheduling software!!", relief=RAISED,font='Helvetica 9 bold', bg="light pink")
		welcome.grid(row=0)
		self.after(3000, welcome.destroy)

		Button(self, text="Log Details", font='Helvetic 10 bold', bg="green", fg="white", command=lambda:[master.switch_frame(page_admin_log)]).grid(row=1)
		Label(self, text="").grid(row=2)
		Button(self, text="Employee Details", font='Helvetic 10 bold', bg="green", fg="white", command=lambda:[master.switch_frame(page_admin_emp)]).grid(row=3)
		Label(self, text="").grid(row=4)
		Button(self, text="Training details", font='Helvetic 10 bold', bg="green", fg="white", command=lambda:[master.switch_frame(page_admin_training)]).grid(row=5)
		Button(self, text="Logout",  font='Helvetic 10 bold', bg="blue", fg="white", command=lambda:[master.switch_frame(signin_page)]).grid(row=0, column=2)

class page_admin_log(LabelFrame):
	def __init__(self, master):
		LabelFrame.__init__(self, master)
		#take input of file
		Label(self, text="employee id").grid(row=1)
		T = Text(self, width=5, height=8)
		T.grid(row=2)
		T.insert(END, "FILE")
		Button(self, text="OK", font='Helvetic 10 bold', bg="light blue", fg="white", command=lambda:[master.switch_frame(main_page_admin)]).grid(row=3)

class page_admin_emp(LabelFrame):
	def __init__(self, master):
		LabelFrame.__init__(self, master)
		
		Label(self, text="employee_id", font='Helvetica 12 bold').grid(row=1)
		self.employee_id = Entry(self, textvariable="employee_id")
		self.employee_id.config(highlightthickness=1, highlightcolor= "black", bg="light grey")
		self.employee_id.grid(row=2)
		Label(self, text="").grid(row=3)

		Button(self, text="SUBMIT", font='Helvetic 10 bold', bg="light green", fg="white").grid(row=4)
		Button(self, text="Go back",  font='Helvetic 10 bold', bg="blue", fg="white", command=lambda:[master.switch_frame(main_page_admin)]).grid(row=1, column=3)
		
	def get_details(self):
		q1='SELECT * FROM employee WHERE emp_id=%s'
		mycursor.execute(q1, (self.employee_id, ))
		employee = mycursor.fetchall()
		return list(employee)

	def fill_textarea(self):	
		self.Label(self, text="employee id").grid(row=5)	
		details_list = ["Employee_id", "Name", "Role_id", "Skillset"]
		text_details = self.get_details()
		for i in range(4):
			Label(self, text=details_list[i]).grid(row=i+1+5, column=1)
			T = Text(self, width=5, height=5)
			T.grid(row=i+1+5, column=2)
			T.insert(END, text_details[i])

class page_admin_training(LabelFrame):
	def __int__(self, master):
		LabelFrame.__init__(self, master)
		Button(self, text="Go back", font='Helvetic 10 bold', bg="blue", fg="white", command=lambda:[master.switch_frame(main_page_admin)]).grid(row=0)	
		q = 'SELECT training, skills FROM training'
		mycursor.execute(q)
		result = mycursor.fetchall()
		for i in range(len(result)):
			Label(self, text=result[i][0]).grid(row=i, column=1)
			T = Text(self, width=7)
			T.grid(row=i, column=2)
			T.insert(END, result[i][1])
			

    		

		

if __name__=="__main__":
	app = window()
	app.mainloop()


mydb.close()


#https://pynative.com/basic-python-quiz-for-beginners/
