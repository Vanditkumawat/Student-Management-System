from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root,text ="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg = "Black")
        title.pack(side = TOP,fill=X)
        #====================All Variables=================================
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_no_var = StringVar()
        self.dob_var = StringVar()



        #====================Manage_frame==================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey13")
        Manage_Frame.place(x=0,y=80,width=450,height=720)

        M_title=Label(Manage_Frame,text="Manage Students",bg="grey13",fg="white",font=("times new roman",30,"bold"))
        M_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="grey13", fg="white",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10 ,padx=20,sticky="w")

        txt_roll = Entry(Manage_Frame,textvariable=self.roll_no_var, font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="grey13", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_emailid = Label(Manage_Frame, text="Email Id", bg="grey13", fg="white", font=("times new roman", 20, "bold"))
        lbl_emailid.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_emailid = Entry(Manage_Frame,textvariable=self.email_var,  font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_emailid.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="grey13", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var, font=("times new roman", 14 , "bold"),state="readonly")
        combo_gender["values"] = ("Male","Female")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contact_no = Label(Manage_Frame, text="Contact No.", bg="grey13", fg="white",font=("times new roman", 20, "bold"))
        lbl_contact_no.grid(row=5, column=0, pady=10 ,padx=20,sticky="w")

        txt_contact_no = Entry(Manage_Frame,textvariable=self.contact_no_var,  font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_contact_no.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="grey13", fg="white",font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10 ,padx=20,sticky="w")

        txt_DOB = Entry(Manage_Frame,textvariable=self.dob_var,  font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="grey13", fg="white",font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10 ,padx=20,sticky="w")

        txt_address = Text(Manage_Frame, width =30,height = 6, font=("",10))
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
        #====================Button frame===================================

        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE,bg="grey13")
        btn_frame.place(x=10,y=600,width = 410)
        addbtn = Button(btn_frame,text="Add",width = 10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10).grid(row=0, column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10).grid(row=0, column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10).grid(row=0, column=3,padx=10,pady=10)

        #====================Detail_frame==================================


        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey42")
        Detail_Frame.place(x=450,y=80,width=1080,height=720)

        lbl_search_by = Label(Detail_Frame, text="Search By", bg="grey42", fg="white", font=("times new roman", 20, "bold"))
        lbl_search_by.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman", 14, "bold"),state="readonly")
        combo_Search["values"] = ("Roll No.","Name","Contact No.")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Text(Detail_Frame,width=17,height=1,font=("times new roman", 14, "bold"),bd=5 ,relief =GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame,text="Search",width = 10,pady =5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5).grid(row=0, column=4,padx=10,pady=10)
        #===================================Table frame=============================================
        TABLE_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey42")
        TABLE_Frame.place(x=460,y=150,width=1060,height=630)
        scroll_x = Scrollbar(TABLE_Frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(TABLE_Frame,orient = VERTICAL)
        student_table =ttk.Treeview(TABLE_Frame , columns=("roll no.","name","email id","gender","contact no.","dob","address"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = student_table.xview)
        scroll_y.config(command = student_table.yview)
        student_table.heading("roll no.",text = "Roll No.")
        student_table.heading("name",text = "Name")
        student_table.heading("email id",text = "Email Id")
        student_table.heading("gender",text = "Gender")
        student_table.heading("contact no.",text = "Contact No." )
        student_table.heading("dob",text = "D.O.B")
        student_table.heading("address",text = "Address")
        student_table["show"]="headings"                   ###treeview also show index column so to remove that column we use this statement
        student_table.column("roll no.", width=120)
        student_table.column("name", width=130)
        student_table.column("email id", width=150)
        student_table.column("gender", width=100)
        student_table.column("contact no.", width=120)
        student_table.column("dob", width=110)
        student_table.column("address", width=290)
        student_table.pack(fill=BOTH,expand=1)

    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students value(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
        self.name_var.get(),
        self.email_var.get(),
        self.gender_var.get(),
        self.contact_no_var.get(),
        self.dob_var.get(),
        self.txt_address.get('1.0',END)))
        con.commit()
        con.close()
    def Fetch_data(self):
        con = pymysql.connect(host="127.0.0.1", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()


root =Tk()
S1 = Student(root)
root.mainloop()