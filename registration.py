from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk  # pip install Pillow
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration windows")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # ======Backhround Image======
        self.bg = ImageTk.PhotoImage(file="images/pic.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # ======Side bar/Image======
        self.left=ImageTk.PhotoImage(file="images/ddddd.jpg")
        left=Label(self.root,image=self.left).place(x=70,y=100,width=500,height=500)

        # ======Registration Frame======
        frame1=Frame(self.root,bg="white")
        frame1.place(x=550,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTRATION HERE",font=("times new roman", 20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #_____Form text filed___________row 1
        # self.var_fname=StringVar()
        f_name=Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130,width=250)

        #________row 2
        Contact=Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200,width=250)

        # ________row 3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.cmb_quest=ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['value']=("Select" ,"your First pet Name", "Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ________row 2
        Password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place( x=50,y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        Password2 = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpasswoed = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpasswoed.place(x=370, y=340, width=250)

        #___TERMS_____
        self.var_chk=IntVar()
        chk= Checkbutton(frame1,text="I Agree the Terms & Condition",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_registration=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_login = Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2").place(x=230, y=500,width=180)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpasswoed.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpasswoed.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpasswoed.get():
            messagebox.showerror("Error","Password & Confirm Password Should be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to:{str(es)} ",parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()