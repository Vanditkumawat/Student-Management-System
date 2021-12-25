from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
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
        self.search_by = StringVar()

        self.search_txt = StringVar()

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
        updatebtn = Button(btn_frame, text="Update",command=self.update_data, width=10).grid(row=0, column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame, text="Delete",command = self.delete_data1, width=10).grid(row=0, column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame, text="Clear",command=self.clear, width=10).grid(row=0, column=3,padx=10,pady=10)

        #====================Detail_frame==================================


        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey42")
        Detail_Frame.place(x=450,y=80,width=1080,height=720)

        lbl_search_by = Label(Detail_Frame, text="Search By", bg="grey42", fg="white", font=("times new roman", 20, "bold"))
        lbl_search_by.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman", 14, "bold"),state="readonly")
        combo_Search["values"] = ("Roll No.","Name","Contact No.")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Text(Detail_Frame,textvariable=self.search_txt,width=17,height=1,font=("times new roman", 14, "bold"),bd=5 ,relief =GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame,text="Search",width = 10,pady =5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4,padx=10,pady=10)
        #===================================Table frame=============================================
        TABLE_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey42")
        TABLE_Frame.place(x=460,y=150,width=1060,height=630)
        scroll_x = Scrollbar(TABLE_Frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(TABLE_Frame,orient = VERTICAL)
        self.student_table =ttk.Treeview(TABLE_Frame , columns=("roll no.","name","email id","gender","contact no.","dob","address"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("roll no.",text = "Roll No.")
        self.student_table.heading("name",text = "Name")
        self.student_table.heading("email id",text = "Email Id")
        self.student_table.heading("gender",text = "Gender")
        self.student_table.heading("contact no.",text = "Contact No." )
        self.student_table.heading("dob",text = "D.O.B")
        self.student_table.heading("address",text = "Address")
        self.student_table["show"]="headings"                   ###treeview also show index column so to remove that column we use this statement
        self.student_table.column("roll no.", width=120)
        self.student_table.column("name", width=130)
        self.student_table.column("email id", width=150)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact no.", width=120)
        self.student_table.column("dob", width=110)
        self.student_table.column("address", width=290)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
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
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.roll_no_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_no_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete('1.0', END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row=content["values"]
        self.roll_no_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_no_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete('1.0', END)
        self.txt_address.insert('1.0', row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email_id=%s,gender=%s,contact_no=%s,dob=%s,address=%s where roll_no=%s",
                    (self.name_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_no_var.get(),
                     self.dob_var.get(),
                     self.txt_address.get('1.0', END),
                     self.roll_no_var.get()
                     ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data1(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students"+str(self.search_by.get())+"like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()


root =Tk()
S1 = Student(root)
root.mainloop()