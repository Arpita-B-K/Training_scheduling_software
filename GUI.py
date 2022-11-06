from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class window(Tk):
	def __init__(self):
		Tk.__init__(self)
		Label(self, text="SCHEDULING SOFTWARE", font='Helvetica 18 bold').pack()
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
		Label(self, text="Please enter your to Signup details", font='Helvetica 12 bold').grid(row=0)
		#empty space
		Label(self, text="").grid(row=1)

		#label and entry box for NAME
		Label(self, text="NAME", font='Helvetica 12 bold').grid(row=2)
		self._name_signup_entry = Entry(self, textvariable="name_signup")
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
			Radiobutton(self, text=usrty, font='Helvetica 10 bold', activebackground="green", indicatoron = 0, width = 10, padx = 5 ,variable=self._usertype_signup_entry, value=val).grid(row=val+5)	

		#empty space
		Label(self, text="").grid(row=9)

		#label and entry box for USERNAME
		Label(self, text="USERNAME", font='Helvetica 12 bold').grid(row=10)
		self._username_signup_entry = Entry(self, textvariable="username_signup")
		self._username_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._username_signup_entry.grid(row=11)
		#empty space
		Label(self, text="").grid(row=12)

		#label and entry box for PASSWORD
		Label(self, text="PASSWORD", font='Helvetica 12 bold').grid(row=13)
		self._password_signup_entry = Entry(self, textvariable="password_signup", show= '*')
		self._password_signup_entry.config(highlightthickness=1, highlightcolor= "black")
		self._password_signup_entry.grid(row=14)

		#self.mandatory_entry(self.password_signup_entry)
		#empty space
		Label(self, text="").grid(row=15)

		#Signup button
		Button(self, text="SIGNUP", bg="lightblue", fg="black",borderwidth=4, width=10,
                       relief=GROOVE, highlightthickness=1, highlightcolor= "blue",command=lambda: [self.mandatory_entry(master)]).grid(row=16)

	def mandatory_entry(self, master):
    	#appending all entry widgets to a list	
		entry_list = []
		entry_list.append(self._name_signup_entry)
		entry_list.append(self._username_signup_entry)
		entry_list.append(self._password_signup_entry)
		entry_list.append(self._usertype_signup_entry)
		count = 0
		#checking entry field, if the entry is filled,then count increment or else pop a messagebox telling user to fill that field
		for i in entry_list:
			if i.get():
				count+=1
			

		#if all entry box are entered reset all entry boxes to empty fields and switch frame to signin_page
		if count==4:
			for i in range(len(entry_list)-1):
				entry_list[i].delete(0, END)
			entry_list[-1].set(0)
			master.switch_frame(signin_page)
		else:
			messagebox.showerror("showerrormandatoryfields", "Information\nPlease enter the mandatory fields")
			
			

class signin_page(LabelFrame):
	def __init__(self, master):
		#creating a frame inside main window
		LabelFrame.__init__(self, master)
		
		#display label text
		Label(self, text="Please enter login details", font='Helvetica 12 bold').grid(row=0)
		#empty space
		Label(self, text="").grid(row=1)
		
		#USERNAME label display
		Label(self, text="USERNAME", font='Helvetica 12 bold').grid(row=2)
		#box for taking entry from user for username
		self._username_login_entry = Entry(self, textvariable="username")
		self._username_login_entry.config(highlightthickness=1, highlightcolor= "black")
		self._username_login_entry.grid(row=3)
		#empty space
		Label(self, text="").grid(row=4)
		
		#PASSWORD label display
		Label(self, text="PASSWORD", font='Helvetica 12 bold').grid(row=5)
		#box for taking entry from user for password
		self._password__login_entry = Entry(self, textvariable="password", show= '*')
		self._password__login_entry.config(highlightthickness=1, highlightcolor= "black")
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
		Button(self, text="Login",width=10, height=1, bg="green", fg="white", borderwidth=4,
                       relief=GROOVE, command=lambda: [self.mandatory_entry(master)]).grid(row=12)
		#empty space
		Label(self, text="").grid(row=13)
		
		#goto signup page
		Button(self, text="Don't have account?Signup",font= ('Helvetica 8 underline'),fg="blue", highlightthickness=1, highlightcolor= "blue", command= lambda:[master.switch_frame(signup_page)]).grid(row=14)
		Frame.pack(self, padx=40, pady=40)
	def mandatory_entry(self, master):

		entry_list = []
		entry_list.append(self._username_login_entry)
		entry_list.append(self._password__login_entry)
		entry_list.append(self._usertype_login_entry)
		count = 0
		for i in entry_list:
			if i.get():
				count+=1
			

		if count==3:
			for i in range(len(entry_list)-1):
				entry_list[i].delete(0, END)
			entry_list[-1].set(0)
			master.switch_frame(main_page)
		else:
			messagebox.showerror("showerrormandatoryfields", "Error\nPlease fill the mandatory fields")	
    		
    			

class main_page(LabelFrame):
	def __init__(self, master):
    	#creating  a new frame
		LabelFrame(width=600, height=600).__init__(self, master)
		#display TASK LISt text
		Label(self, text="Task list", width=10, font=('Helvetica 14 underline')).grid(row=2, column=1)
		#empty space
		Label(self, text="").grid(row=3, column=1)	
		#buttons lists of task list	
		task_list = []
		task_list.append("Task1")
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
		T = Text(self, height = 1, width = 10, relief=GROOVE)
		T.grid(row=3, column=8)
		T.insert(END, "name")
		#STARTDATE
		Label(self, text="Startdate:", font=('Helvetica 10 bold')).grid(row=4, column=7)
		#textbox for startdate
		T = Text(self, height = 1, width = 10, relief=GROOVE)
		T.grid(row=4, column=8)
		T.insert(END, "startdate")
		#DUEDATE
		Label(self, text="Duedate:", font=('Helvetica 10 bold')).grid(row=5, column=7)
		#textbox for duedate
		T = Text(self, height = 1, width = 10, relief=GROOVE)
		T.grid(row=5, column=8)
		T.insert(END, "duedate")
		#INFO
		Label(self, text="Info:", font=('Helvetica 10 bold')).grid(row=6, column=7)
		#textbox for info
		T = Text(self, height = 1, width = 10, relief=GROOVE)
		T.grid(row=6, column=8)
		T.insert(END, "info")
		#empty space
		Label(self, text="").grid(row=7, column=8)
		#button for take test function
		Button(self, text="Take Test", width=10, bg="green", fg="black", borderwidth=4,
                       relief=GROOVE, command=lambda:[], font=('Helvetica 10 bold')).grid(row=8, column=8)

		#button for logging out 
		Button(self, text="Logout", bg="blue", fg="white", borderwidth=4,
                       relief=GROOVE, command=lambda: master.switch_frame(signin_page), font=('Helvetica 10 bold')).grid(row=9, column=5)

if __name__=="__main__":
	app = window()
	app.geometry("500x500")
	app.mainloop()