
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



class signup_page(LabelFrame):
	def __init__(self, master):
		#creating a frame inside main window
		LabelFrame.__init__(self, master)
		
		#display label text
		Label(self, text="Please enter your Signup details", font='Helvetica 12 bold', bg="light blue").grid(row=0)
		#empty space
		Label(self, text="").grid(row=1)

		#label and entry box for NAME
		Label(self, text="NAME", font='Helvetica 12 bold').grid(row=2)
		self._name_signup_entry = Entry(self, textvariable="name_signup", bg="light grey")
		self._name_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._name_signup_entry.grid(row=3)
		#empty space
		Label(self, text="").grid(row=4)

		#label and entry box for USERTYPE
		Label(self, text="USERTYPE", font='Helvetica 12 bold').grid(row=5)
		self._usertype_signup_entry = IntVar()
		usertypes = [("Employee", 1),
					("HR", 2),
					("Admin", 3)]
		for usrty, val in usertypes:
			Radiobutton(self, text=usrty, font='Helvetica 10 bold', activebackground="light grey", indicatoron = 0, width = 10, padx = 5 ,variable=self._usertype_signup_entry, value=val).grid(row=val+5)	

		#empty space
		Label(self, text="").grid(row=9)

		#label and entry box for USERNAME
		Label(self, text="USERNAME", font='Helvetica 12 bold').grid(row=10)
		self._username_signup_entry = Entry(self, textvariable="username_signup", bg="light grey")
		self._username_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._username_signup_entry.grid(row=11)
		#empty space
		Label(self, text="").grid(row=12)

		#label and entry box for PASSWORD
		Label(self, text="PASSWORD", font='Helvetica 12 bold').grid(row=13)
		self._password_signup_entry = Entry(self, textvariable="password_signup", show= '*', bg="light grey")
		self._password_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._password_signup_entry.grid(row=14)

		#self.mandatory_entry(self.password_signup_entry)
		#empty space
		Label(self, text="").grid(row=15)

		#Signup button
		Button(self, text="SIGNUP", bg="blue", fg="white",borderwidth=4, width=10, font='helvetica 10 bold',
                       relief=GROOVE, highlightthickness=1, highlightcolor= "blue",command=lambda: self.mandatory_entry(master)).grid(row=16)

	
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
		q1="SELECT * FROM credentials WHERE username=%s"
	
		mycursor.execute(q1, (entry_list_val[1],))
		ans1=mycursor.fetchall()
		if ans1==[]:
			hashed_password=self.encrypt_password(entry_list_val[2])	
			q2='insert into credentials (name, username, password, user_type) values (%s, %s, %s, %s)'
			val2=(entry_list_val[0],entry_list_val[1], hashed_password, entry_list_val[3])
			mycursor.execute(q2, val2)
			mydb.commit()
			print(mycursor.rowcount, "record inserted.")
		else:
			answer=messagebox.askyesno("useralreadyexists","ERROR!\nUser with this username already exists\nTry with another username\nDO YOU ALREADY HAVE AN ACCOUNT?")
			if answer:
				master.switch_frame(signin_page)

	
	def mandatory_entry(self, master):
    	#appending all entry widgets to a list	
		entry_list = []
		entry_list.append(self._name_signup_entry)
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
		if count==4:
			self.add_credentials(entry_list, master)
			#for i in range(len(entry_list)-1):
			#	entry_list[i].delete(0, END)
			#entry_list[-1].set(0)
			#master.switch_frame(signin_page)
		else:
			messagebox.showerror("showerrormandatoryfields", "Information\nPlease enter the mandatory fields")
	def encrypt_password(self, password):
		password = password.encode("utf-8")
		encoded_text = hashlib.md5(password).hexdigest()		
		return encoded_text
			
emp_id = ""			

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
		Button(self, text="Don't have account?Signup",font= ('Helvetica 8 underline'),fg="blue", highlightthickness=1, highlightcolor= "blue", command= lambda:[master.switch_frame(signup_page)]).grid(row=14)

		

	def check_cred(self, entry_list, master):
    	#check for same username in the database
		# if found check for password  Then if both are correct switch to main page of that usertype else display message invalid credentials
		entry_list_val=[]
		for i in entry_list:
			entry_list_val.append(i.get())
		entry_list_val[1]=self.encrypt_password(entry_list_val[1])

		q1='SELECT * FROM credentials WHERE username=%s'
		mycursor.execute(q1, (entry_list_val[0],))
		myresult = mycursor.fetchone()
		if myresult!=[]:
			myresult=list(myresult)	
			emp_id = myresult[0]
			user_type = entry_list_val[-1]
			del myresult[0:2]
			del myresult[-1]
			del entry_list_val[-1]
			if myresult==entry_list_val:
				if user_type==1:
					master.switch_frame(main_page_emp)
				elif user_type==2:
					master.switch_frame(main_page_hr)
				elif user_type==3:
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
			#for i in range(len(entry_list)-1):
			#	entry_list[i].delete(0, END)
			#entry_list[-1].set(0)
						
		else:
			messagebox.showerror("showerrormandatoryfields", "Error\nPlease fill the mandatory fields")	
		
	def encrypt_password(self, password):
			password = password.encode("utf-8")
			encoded_text = hashlib.md5(password).hexdigest()		
			return encoded_text			

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
		task_list = []
		#task_list.append("Task1")
		task_list.append("Task2")
		task_list.append("Task3")
		task_list.append("Task4")
		for i in range(len(task_list)):
			Button(self, text=task_list[i], width=10, font=('Helvetica 10 bold')).grid(row=4+i, column=1)

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
		Button(self, text="Logout", bg="blue", fg="white", borderwidth=4,
                       relief=GROOVE, command=lambda: master.switch_frame(signin_page), font=('Helvetica 10 bold')).grid(row=9, column=5)

if __name__=="__main__":
	app = window()
	app.geometry("500x500")
	app.mainloop()

mydb.close()