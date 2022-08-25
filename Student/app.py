############################################CREATED BY MUHAMMAD HANAN ASGHAR#################################
from tkinter import *
import tkinter.messagebox as tmsg
import sqlite3 as sq
from collections import OrderedDict
import tkinter.ttk as ttk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("Student Management(Login Page)")
        self.conStart()
        self.user = StringVar()
        self.passw = StringVar()


        #=================Frame
        login_frame = Frame(self.root,bg = "#8E44AD")
        login_frame.place(x=0,y=0,width = 800,height = 50)
        title_login = Label(login_frame,text = "Login Page",font=("lucida",25,"bold"),fg = "white",bg = "#8E44AD")
        title_login.pack()
        #=============Main Frame
        main_frame = Frame(self.root,bd = 7,relief = RIDGE)
        main_frame.place(x = 5,y = 55,width = 786,height = 435)
        #==============UsernAME TEXTFIELD AND LABEL
        user_lbl = Label(main_frame,text = "Username",font=("lucida",15,'bold'),fg = "#8E44AD")
        user_lbl.grid(row = 1,column = 1,padx = 40,pady = 40)
        user_field = Entry(main_frame,textvariable = self.user)
        user_field.grid(row = 1,column = 2,ipady = 7,ipadx = 20,padx = 40)
        #=======================PASSWORD LABEL AND TEXTFIELD
        pass_lbl = Label(main_frame,text="Password",font=("lucida",15,"bold"),fg = "#8E44AD")
        pass_lbl.grid(row = 2,column = 1,pady = 40)
        pass_field = Entry(main_frame,textvariable = self.passw)
        pass_field.grid(row = 2,column = 2,ipady = 7,ipadx = 20,padx = 40)
        #=====================LOGIN AND REGISTIRATION
        login_btn = Button(main_frame,text = "Login",font=("lucida",10,"bold"),bg = "#8E44AD",fg = "white",bd = 7,relief = SUNKEN,command = self.get)
        login_btn.grid(row = 3,column = 1,ipady = 4,ipadx = 13,pady = 40,padx = 40)
        reg_btn = Button(main_frame,text = "Register",font=("lucida",10,"bold"),bg = "#8E44AD",fg = "white",bd = 7,relief = SUNKEN,command = self.post)
        reg_btn.grid(row = 3,column = 2,ipady = 4,ipadx = 13,pady = 40)
#Move to Second Screen
    def secondScreen(self):
        root2 = Toplevel(self.root)
        enter = EnterData(root2)
        #==========================Creating Tables
    def conStart(self):
        con = sq.connect("data.db")
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logina(
            user TEXT NOT NULL,
            pass TEXT NOT NULL
            )
        """)
        con.commit()
        con.close()
        #=============================Putting Data
    def post(self):
        a = self.user.get()
        b = self.passw.get()
        con = sq.connect("data.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM logina")
        data = cursor.fetchall()
        data_imp = OrderedDict(data)
        if (self.user.get() in data_imp.keys()) and (self.passw.get() in data_imp.values()):
            self.error2()
        cursor.execute("INSERT INTO logina VALUES(?,?)",(a,b))
        con.commit()
        con.close()
        self.succees2()
        #=============================Getting Data
    def get(self):
        con = sq.connect("data.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM logina")
        data = cursor.fetchall()
        data_imp = OrderedDict(data)
        #======================Condition Checked For Login
        if (self.user.get() in data_imp.keys()) and (self.passw.get() in data_imp.values()):
            self.succees()
        else:
            self.error()



#================================Succees Message
    def succees(self):
        a = tmsg.showinfo('Login Succeesful',"Thanks For Coming Back")
        if a == 'ok':
            self.secondScreen()

#==============================Error Message
    def error(self):
        tmsg.showerror('Error',"Username Not Found")

#====================================Second Error
    def error2(self):
        tmsg.showerror("Error","User Already Found")
#========================================Second Success
    def succees2(self):
        tmsg.showinfo("Succees","Account Create Succeesfully")


#=============================Class For Second Page
class EnterData:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("Student Management(Enter Data)")
        self.dataStart()
        self.name = StringVar()
        self.dob = StringVar()
        self.roll = StringVar()
        self.gen = StringVar()
#============================Enter Data Frame
        data_frame = Frame(self.root,bg = "#B402FE")
        data_frame.place(width = 800,x = 0,y = 0 ,height = 50)
        labl_data = Label(data_frame,bg = "#B402FE",fg = "white",font = ("lucida",25,"bold"),text = "Enter Data")
        labl_data.pack()
#==========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = RIDGE)
        main_frame.place(width = 780,height = 430,x = 8,y = 58)
        labe_tit = Label(main_frame,text = "Student Name",font = ("lucida",15,"bold"))
        labe_tit.grid(row = 0,column = 0,padx = 50,pady = 40)
        #======================User
        tit_en = Entry(main_frame,textvariable = self.name)
        tit_en.grid(row = 0,column = 1,ipady = 7,ipadx = 20)
        #==========================Roll
        roll_lab = Label(main_frame,text = "Roll No",font=("lucida",15,"bold"))
        roll_lab.grid(row=1,column = 0)
        roll_en = Entry(main_frame,textvariable = self.roll)
        roll_en.grid(row = 1,column = 1,ipady = 7,ipadx = 20)
        #=============================Dob
        dob_lab = Label(main_frame,text = "DOB",font=("lucida",15,"bold"))
        dob_lab.grid(row = 2,column = 0,pady = 40)
        dob_en = Entry(main_frame,textvariable = self.dob)
        dob_en.grid(row = 2,column = 1,ipady = 7,ipadx = 20)
        #============================Gender
        gen_lab = Label(main_frame,text = "Gender",font = ("lucida",15,"bold"))
        gen_lab.grid(row = 3,column = 0)
        com = ttk.Combobox(main_frame,state = "readonly",textvariable = self.gen)
        com['values'] = ('Male',"Female","Other")
        com.grid(row = 3,column = 1,ipady = 7,ipadx = 20)
        #==========================Submit Button
        btn_sub = Button(main_frame,text = "Submit",bg = "#B402FE",fg = "white",bd = 0,font = ("lucida",10,"bold"),command = self.enterData)
        btn_sub.grid(row = 4,column = 1,ipady = 7,pady = 40,ipadx = 20)

    def dataStart(self):
            con = sq.connect('data.db')
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stu_data(
                id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                roll TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL
                )
            """)
            con.commit()
            con.close()
    def enterData(self):
        con = sq.connect('data.db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO stu_data VALUES(NULL,?,?,?,?)",(self.name.get(),self.roll.get(),self.dob.get(),self.gen.get()))
        con.commit()
        con.close()
        self.succees()

#================================Succees Message
    def succees(self):
        a = tmsg.showinfo('Succesfull',"Data Inserted")
        if a == 'ok':
            self.askQues()

#====================================Second Error
    def error2(self):
        tmsg.showerror("Error","Data Already Found")

#======================================Ask Question
    def askQues(self):
        a = tmsg.askquestion("Confirm","Are You Want to Go to Details Page?")
        if a == 'yes':
            root3 = Toplevel(self.root)
            show = showData(root3)


class showData:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("Student Management(Details)")
        #==========================Show Frame
        show_frame = Frame(self.root,bg = "#B402FE")
        show_frame.place(width = 800,x = 0,y = 0 ,height = 50)
        labl_show = Label(show_frame,bg = "#B402FE",fg = "white",font = ("lucida",25,"bold"),text = "Details of Students")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 780,height = 430,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        tree['columns'] = ("Name","Roll No","D-O-B","Gender")
        tree.column('#0',width=50,minwidth = 25)
        tree.column('Name',width=50,minwidth = 25)
        tree.column('Roll No',width=50,minwidth = 25)
        tree.column('D-O-B',width=50,minwidth = 25)
        tree.column('Gender',width=50,minwidth = 25)
        tree.heading("#0",text = "ID",anchor = W)
        tree.heading("Name",text = "Name",anchor = W)
        tree.heading("Roll No",text = "Roll No",anchor = W)
        tree.heading("D-O-B",text = "D-O-B",anchor = W)
        tree.heading("Gender",text="Gender",anchor = W)
        con = sq.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM stu_data")
        result = cursor.fetchall()
        for i in result:
            tree.insert("","end",text = f"{i[0]}",values = (f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}'))
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)






if __name__ == "__main__":
    root = Tk()
    l = Login(root)
    root.mainloop()
    
    ############################################CREATED BY MUHAMMAD HANAN ASGHAR#################################
