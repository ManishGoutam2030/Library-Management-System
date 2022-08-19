# Create a database projectx with four tables in MYSQL:
# 1.students:
# create table students (Roll_no int(3) primary key,Sname varchar(30),Branch varchar(30))

# 2.books:
# create table books (Sr_no int(3) auto_increment primary key,Bookname varchar(30),Price int(3),Status varchar(30))

# 3.assignment:
# create table assignment(Srbook int(3),Rstudent int(3),Assign_date date,Submit_date date,Fine int(3),foreign key(Srbook) references books(Sr_no),foreign key(Rstudent) references students(Roll_no))

# 4.display:
# create table display(Serial_bookno int(3),Student_rollno int(3),Assign_date date,Submisson_date date,Fine int(3),Student_status varchar(30),foreign key(Serial_bookno) references books(Sr_no),foreign key(Student_rollno) references students(Roll_no))


from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from datetime import date
db=mysql.connector.connect(host="localhost",user="root",password="root",database='projectx')

def loaddatabooks(cm):
    lst=[]
    cur=db.cursor()
    sql="select Bookname from books"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    cm.config(values=lst)

def loadserialbooks(cm):
    lst=[]
    cur=db.cursor()
    sql="select Sr_no from books"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    cm.config(values=lst)

def assignserialbooks(cm):
    lst=[]
    cur=db.cursor()
    sql="select Srbook from assignment"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    lst=list(set(lst))
    cm.config(values=lst)

def loaddatastudents(cms):
    lst=[]
    cur=db.cursor()
    sql="select Sname from students"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    cms.config(values=lst)
def loadserialstudents(cms):
    lst=[]
    cur=db.cursor()
    sql="select Roll_no from students"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    cms.config(values=lst)
def assignserialstudents(cms):
    
    lst=[]
    cur=db.cursor()
    sql="select Rstudent from assignment"
    cur.execute(sql)
    rs=cur.fetchall()
    for data in rs:
        lst.append(data[0])
    lst=list(set(lst))
    cms.config(values=lst)

def Display_assign_refresh():
    global Display_assign_Display_data,Display_assign_To_date,Display_assign_From_date
    Display_assign_Display_data.delete("1.0",'end')
    Display_assign_From_date.delete("1.0",'end')
    Display_assign_To_date.delete("1.0",'end')

def Display_between():
    global Display_assign_From_date,Display_assign_To_date,Display_assign_Display_data
    try:
        cur=db.cursor()
        Display_between_from_date=Display_assign_From_date.get("1.0","end-1c")
        Display_between_to_date=Display_assign_To_date.get("1.0","end-1c")
        data=(Display_between_from_date,Display_between_to_date)
        sql="select * from display where Assign_date between %s and %s"
        cur.execute(sql,data)
        rs=cur.fetchall()
        for i in rs:
            Display_between_serial_no=""
            a="Sr_no is "+str(i[0])
            for j in a:
                Display_between_serial_no+=j
            Display_between_roll_no="Roll no: "+str(i[1])
            Display_between_assign_date="Assign date: "+str(i[2])
            Display_between_submit_date="Submit date: "+str(i[3])
            Display_between_fine="Fine: "+str(i[4])
            Display_between_status="Student_status: "+str(i[5])
            Display_assign_Display_data.insert(1.0,(Display_between_serial_no,Display_between_roll_no,Display_between_assign_date,Display_between_submit_date,Display_between_fine,Display_between_status))
            Display_assign_Display_data.insert(1.0,'\n')
               
    except TypeError:
        return



def Display_all():
    global Display_assign_Display_data
    try:
        cur=db.cursor()
        sql="select * from display"
        cur.execute(sql)
        rs=cur.fetchall()
        for i in rs:
            Display_all_serial_no=""
            a="Sr_no is "+str(i[0])
            for j in a:
                Display_all_serial_no+=j
            Display_all_roll_no="Roll no is "+str(i[1])
            Display_all_assign_date="Assign date is "+str(i[2])
            Display_all_submit_date="Submit date is "+str(i[3])
            Display_all_fine="Fine is "+str(i[4])
            Display_all_status="Student_status: "+str(i[5])
            Display_assign_Display_data.insert(1.0,(Display_all_serial_no,Display_all_roll_no,Display_all_assign_date,Display_all_submit_date,Display_all_fine,Display_all_status))
            Display_assign_Display_data.insert(1.0,'\n')
               
    except TypeError:
        return

def All_data_display():
    global v
    choice=v.get()
    if(choice==1):
        Display_all()
    elif(choice==2):
        Display_between()

def Display_assign():
    global v,Display_assign_From_date,Display_assign_To_date,Display_assign_Display_data,Display_assign_From_date,Display_assign_to_date
    Top_display_assign=Toplevel(root)
    Top_display_assign.geometry('1500x1500')
    Top_display_assign.title("Display Assigned Books")
    v=IntVar()
    Display_assign_Select_your_choice_heading=Label(Top_display_assign,text="Select your choice",bg='white',fg='red',font=('Arial',27,'bold'))
    Display_assign_Select_your_choice_heading.grid(row=0,column=0,pady=10,padx=10)
    Display_assign_Back_button=Button(Top_display_assign,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_display_assign.destroy)
    Display_assign_Back_button.grid(row=3,column=2,pady=10,padx=10)
    Display_assign_Display_all_books_radiobutton=Radiobutton(Top_display_assign,text="Display all Books",value=1,variable=v,font=('Arial',15,'bold'))
    Display_assign_Display_all_books_radiobutton.grid(row=1,column=0,pady=10,padx=10)
    Display_assign_Display_books_between_dates_radiobutton=Radiobutton(Top_display_assign,text="Display books between dates",value=2,variable=v,font=('Arial',15,'bold'))
    Display_assign_Display_books_between_dates_radiobutton.grid(row=2,column=0,pady=10,padx=10)
    Display_assign_Display_data=Text(Top_display_assign,width=99,height=39,bg='black',fg='white')
    Display_assign_Display_data.grid(row=4,column=1,pady=10,padx=10)
    Display_assign_From_date_heading=Label(Top_display_assign,text="From (yyyy-mm-dd)",font=('Arial',15,'bold'))
    Display_assign_From_date_heading.grid(row=1,column=1,pady=10,padx=10)
    Display_assign_To_date_heading=Label(Top_display_assign,text="To (yyyy-mm-dd)",font=('Arial',15,'bold'))
    Display_assign_To_date_heading.grid(row=1,column=2,pady=10,padx=10)
    Display_assign_From_date=Text(Top_display_assign,width=18,height=2,bg='pale violet red',fg='black')
    Display_assign_To_date=Text(Top_display_assign,width=18,height=2,bg='pale violet red',fg='black')
    Display_assign_From_date.grid(row=2,column=1)
    Display_assign_To_date.grid(row=2,column=2)
    Display_assign_Display_button=Button(Top_display_assign,text="Display",bg='orange',fg='black',font=('Arial',15,'bold'),command=All_data_display)
    Display_assign_Display_button.grid(row=3,column=0,pady=10,padx=10)
    Display_assign_Refresh_button=Button(Top_display_assign,text="Refresh",bg='spring green',fg='black',font=('Arial',15,'bold'),command=Display_assign_refresh)
    Display_assign_Refresh_button.grid(row=3,column=1,pady=10,padx=10)

def Fine():
    global Submit_Book_serial_no,Submit_Roll_no
    cur=db.cursor()
    Fine_book_serial_no=Submit_Book_serial_no.get()
    Fine_roll_no=Submit_Roll_no.get()
    sql1="select Fine from assignment where Srbook=%s and Rstudent=%s "
    data1=(Fine_book_serial_no,Fine_roll_no)
    cur.execute(sql1,data1)
    rs=cur.fetchone()
    Fine_fine=rs[0]
    if(Fine_fine>0):
        res=messagebox.askquestion("You hava a fine of Rs "+str(Fine_fine),"Are you gonna pay ?")
        if(res=='yes'):
            data2=(0,Fine_book_serial_no,Fine_roll_no)    
            sql2="update assignment set Fine=%s where Srbook=%s and Rstudent=%s"
            cur.execute(sql2,data2)
            db.commit()
            messagebox.showinfo("Fine","You have successfully paid the fine")

            sql3="update display set Fine=%s where Serial_bookno=%s and Student_rollno=%s"
            cur.execute(sql3,data2)
            db.commit()
            messagebox.showinfo("Fine","You have successfully paid the fine")    
    else:
        messagebox.showinfo("Fine","No fine")

def Add_fine():
    global Submit_Book_serial_no,Submit_Roll_no,Submit_Additional_fine
    Add_fine_book_serial_no=Submit_Book_serial_no.get()
    Add_fine_roll_no=Submit_Roll_no.get()
    Add_fine_additional_fine=int(Submit_Additional_fine.get("1.0","end-1c"))
    cur=db.cursor()
    sql1="select Fine from assignment where Srbook=%s and Rstudent=%s "
    data1=(Add_fine_book_serial_no,Add_fine_roll_no)
    cur.execute(sql1,data1)
    rs=cur.fetchone()
    fin=rs[0]
    Add_fine_total_fine=fin+Add_fine_additional_fine
    sql2="update assignment set Fine=%s where Srbook=%s and Rstudent=%s"
    data2=(Add_fine_total_fine,Add_fine_book_serial_no,Add_fine_roll_no)    
    cur.execute(sql2,data2)
    db.commit()
    sql3="update display set Fine=%s where Serial_bookno=%s and Student_rollno=%s"
    data3=(Add_fine_total_fine,Add_fine_book_serial_no,Add_fine_roll_no)    
    cur.execute(sql3,data3)
    db.commit()
    messagebox.showinfo("Fine","Fine successfully added")

def Submit_execution():
    global Submit_Book_serial_no,Submit_Roll_no
    cur=db.cursor()
    Submit_execution_book_serial_no=Submit_Book_serial_no.get()
    Submit_execution_roll_no=Submit_Roll_no.get()
    Submit_execution_submit_date=date.today()
    data1=(Submit_execution_submit_date,Submit_execution_book_serial_no,Submit_execution_roll_no)
    sql1="update assignment set Submit_date=%s where Srbook=%s and Rstudent=%s"
    cur.execute(sql1,data1)
    db.commit()

    sql2="update display set Submission_date=%s where Serial_bookno=%s and Student_rollno=%s"
    cur.execute(sql2,data1)
    db.commit()

    sql3="update books set Status='Available' where Sr_no="+str(Submit_execution_book_serial_no)
    cur.execute(sql3)
    db.commit()
    sql4="select datediff(Submit_date,Assign_date) from assignment where Srbook=%s and Rstudent=%s "
    data3=(Submit_execution_book_serial_no,Submit_execution_roll_no)
    cur.execute(sql4,data3)
    rs=cur.fetchone()
    data=rs[0]
    if(data>15):
        Submit_execution_fine=(data-15)*2
        data4=(Submit_execution_fine,Submit_execution_book_serial_no,Submit_execution_roll_no)
        sql5="update assignment set Fine=%s where Srbook=%s and Rstudent=%s"
        cur.execute(sql5,data4)
        db.commit()

        sql6="update display set Fine=%s where Serial_bookno=%s and Student_rollno=%s"
        cur.execute(sql6,data4)
        db.commit()

        res=messagebox.askquestion("You hava a fine of Rs "+str(Submit_execution_fine),"Are you gonna pay ?")
        if(res=='yes'):
            data5=(0,Submit_execution_book_serial_no,Submit_execution_roll_no)    
            sql7="update assignment set Fine=%s where Srbook=%s and Rstudent=%s"
            cur.execute(sql7,data5)
            db.commit()

            sql8="update display set Fine=%s where Serial_bookno=%s and Student_rollno=%s"
            cur.execute(sql8,data5)
            db.commit()    
    else:
        messagebox.showinfo("Fine","No fine")
    messagebox.showinfo("Submitted","Book Submitted")

def Submit():
    global Submit_Book_serial_no,Submit_Roll_no,Submit_Additional_fine
    Top_submit=Toplevel(root)
    Top_submit.geometry("1500x1500")
    Top_submit.title("Submit")
    Lets_submit_heading=Label(Top_submit,text="Let's Submit :--------",font=('Arial',35,'italic','bold'),fg='green')
    Lets_submit_heading.grid(row=0,column=0)
    Submit_Book_serial_no_heading=Label(Top_submit,text='Book Serial No',font=('Arial',20,'bold'),bg='white',fg='black')
    Submit_Book_serial_no_heading.grid(row=5,column=1,pady=10)
    Submit_Book_serial_no=ttk.Combobox(Top_submit,width=25,height=15,font=('Arial',15,'italic','bold'))
    Submit_Book_serial_no.grid(row=5,column=3,pady=30)
    Submit_Roll_no_heading=Label(Top_submit,text='Roll Number',font=('Arial',20,'bold'),bg='white',fg='black')
    Submit_Roll_no_heading.grid(row=6,column=1,pady=30)
    Submit_Roll_no=ttk.Combobox(Top_submit,width=25,height=15,font=('Arial',15,'italic','bold'))
    Submit_Roll_no.grid(row=6,column=3,pady=30)
    assignserialbooks(Submit_Book_serial_no)
    assignserialstudents(Submit_Roll_no)
    Submit_Additional_fine_heading=Label(Top_submit,text='Additional Fine',font=('Arial',20,'bold'),bg='white',fg='black')
    Submit_Additional_fine_heading.grid(row=7,column=1,pady=10)
    Submit_Additional_fine=Text(Top_submit,width=15,height=2,font=('Arial',15,'italic','bold'))
    Submit_Additional_fine.grid(row=7,column=3,pady=30,padx=10)
    Submit_Submit_button=Button(Top_submit,text='Submit',font=('Arial',30,'italic'),bg='black',fg='white',command=Submit_execution)
    Submit_Submit_button.grid(row=8,column=2,pady=30)
    Submit_Add_a_fine_button=Button(Top_submit,text="Add a Fine",bg='spring green',fg='black',font=('Arial',15,'bold'),command=Add_fine)
    Submit_Add_a_fine_button.grid(row=7,column=4,pady=30,padx=10)
    Submit_Submit_button=Button(Top_submit,text="Fine",bg='red',fg='white',font=('Arial',15,'bold'),command=Fine)
    Submit_Submit_button.grid(row=8,column=3,pady=30)
    Submit_Back_button=Button(Top_submit,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_submit.destroy)
    Submit_Back_button.place(x=1350,y=800)

def Refresh_search_student():
    global Search_student_Student_name,Search_student_Student_roll_no,Search_student_Display_roll_no,Search_student_Display_student_name,Search_student_Display_branch,Search_student_execution_Student_name
    Search_student_Display_roll_no.config(state=NORMAL)
    Search_student_Display_roll_no.delete("1.0","end")
    Search_student_Display_student_name.config(state=NORMAL)
    Search_student_Display_student_name.delete("1.0","end")
    Search_student_Display_branch.config(state=NORMAL)
    Search_student_Display_branch.delete("1.0","end")
    Search_student_Student_name.delete(0,END)
    Search_student_Student_roll_no.delete(0,END)

def Search_student_execution():
    global Search_student_Student_name,Search_student_Student_roll_no,Search_student_Display_roll_no,Search_student_Display_student_name,Search_student_Display_branch
    cur=db.cursor()
    Search_student_execution_student_name=Search_student_Student_name.get()
    Search_student_execution_roll_no=Search_student_Student_roll_no.get()
    data=(Search_student_execution_student_name,Search_student_execution_roll_no)
    sql="select * from students where Sname=%s or Roll_no=%s"
    cur.execute(sql,data)
    rs=cur.fetchone()
    Search_student_Display_roll_no.insert("1.0",rs[0])
    Search_student_Display_roll_no.config(state=DISABLED)
    Search_student_Display_student_name.insert("1.0",rs[1])
    Search_student_Display_student_name.config(state=DISABLED)
    Search_student_Display_branch.insert("1.0",rs[2])
    Search_student_Display_branch.config(state=DISABLED)

def Search_student():
    global Search_student_Student_name,Search_student_Student_roll_no,Search_student_Display_roll_no,Search_student_Display_student_name,Search_student_Display_branch
    Top_search_student=Toplevel(root)
    Top_search_student.geometry("1500x1500")
    Top_search_student.title("Search a Student")
    Search_student_Student_name_heading=Label(Top_search_student,text='Student Name',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_student_Student_name_heading.grid(row=2,column=2,pady=30)
    Search_student_Student_name=ttk.Combobox(Top_search_student,width=25,height=15,font=('Arial',15,'italic','bold'))
    Search_student_Student_name.grid(row=2,column=3,pady=30)
    Search_student_Or=Label(Top_search_student,text='Or',font=('Arial',27,'bold'),bg='white',fg='red')
    Search_student_Or.grid(row=3,column=2,pady=30,padx=20)
    Search_student_Student_roll_no_heading=Label(Top_search_student,text='Student Roll No',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_student_Student_roll_no_heading.grid(row=4,column=2,pady=30)
    Search_student_Student_roll_no=ttk.Combobox(Top_search_student,width=25,height=15,font=('Arial',15,'italic','bold'))
    Search_student_Student_roll_no.grid(row=4,column=3,pady=30)
    Search_student_Search_button=Button(Top_search_student,text='Search',font=('Arial',25,'italic'),fg='white',bg='black',command=Search_student_execution)
    Search_student_Search_button.grid(row=5,column=3,pady=30)
    loaddatastudents(Search_student_Student_name)
    loadserialstudents(Search_student_Student_roll_no)
    Search_student_Display_roll_no_heading=Label(Top_search_student,text='Roll Number',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_student_Display_roll_no_heading.grid(row=8,column=2,pady=30,padx=20)
    Search_student_Display_roll_no=Text(Top_search_student,width=28,height=2.5,bg='cyan',font=25)
    Search_student_Display_roll_no.grid(row=9,column=2,pady=30,padx=20)
    Search_student_Display_student_name_heading=Label(Top_search_student,text='Student Name',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_student_Display_student_name_heading.grid(row=8,column=3,pady=30,padx=20)
    Search_student_Display_student_name=Text(Top_search_student,width=28,height=2.5,bg='cyan',font=25)
    Search_student_Display_student_name.grid(row=9,column=3,pady=30,padx=20)
    Search_student_Display_branch_heading=Label(Top_search_student,text='Branch',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_student_Display_branch_heading.grid(row=8,column=4,pady=30,padx=20)
    Search_student_Display_branch=Text(Top_search_student,width=28,height=2.5,bg='cyan',font=25)
    Search_student_Display_branch.grid(row=9,column=4,pady=30,padx=20)
    Search_student_Display_refresh_button=Button(Top_search_student,text="Refresh",bg='lawn green',fg='black',font=('Arial',25,'bold'),command=Refresh_search_student)
    Search_student_Display_refresh_button.grid(row=10,column=3,pady=30,padx=20)
    Search_student_Display_back_button=Button(Top_search_student,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_search_student.destroy)
    Search_student_Display_back_button.place(x=1350,y=800)

def Refresh_search_book():
    global Search_book_Book_name,Search_book_Book_serial_no,Search_book_Display_book_serial_no,Search_book_Display_book_name,Search_book_Display_price,Search_book_Display_status
    Search_book_Display_book_serial_no.config(state=NORMAL)
    Search_book_Display_book_serial_no.delete("1.0","end")
    Search_book_Display_book_name.config(state=NORMAL)
    Search_book_Display_book_name.delete("1.0","end")
    Search_book_Display_price.config(state=NORMAL)
    Search_book_Display_price.delete("1.0","end")
    Search_book_Display_status.config(state=NORMAL)
    Search_book_Display_status.delete("1.0","end")
    Search_book_Book_name.delete(0,END)
    Search_book_Book_serial_no.delete(0,END)

def Search_book_execution():
    global Search_book_Book_name,Search_book_Book_serial_no,Search_book_Display_book_serial_no,Search_book_Display_book_name,Search_book_Display_price,Search_book_Display_status
    cur=db.cursor()
    Search_book_execution_book_name=Search_book_Book_name.get()
    Search_book_execution_serial_no=Search_book_Book_serial_no.get()
    data1=(Search_book_execution_book_name,Search_book_execution_serial_no)
    sql1="select * from books where Bookname=%s or Sr_no=%s"
    cur.execute(sql1,data1)
    rs=cur.fetchone()
    Search_book_Display_book_serial_no.insert("1.0",rs[0])
    Search_book_Display_book_serial_no.config(state=DISABLED)
    Search_book_Display_book_name.insert("1.0",rs[1])
    Search_book_Display_book_name.config(state=DISABLED)
    Search_book_Display_price.insert("1.0",rs[2])
    Search_book_Display_price.config(state=DISABLED)
    Search_book_Display_status.insert("1.0",rs[3])
    Search_book_Display_status.config(state=DISABLED)

def Search_book():
    global Search_book_Book_name,Search_book_Book_serial_no,Search_book_Display_book_serial_no,Search_book_Display_book_name,Search_book_Display_price,Search_book_Display_status
    Top_search_book=Toplevel(root)
    Top_search_book.geometry("1500x1500")
    Top_search_book.title("Search a Book")
    Search_book_Book_name_heading=Label(Top_search_book,text='Bookname',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Book_name_heading.grid(row=1,column=1,pady=30,padx=20)
    Search_book_Book_name=ttk.Combobox(Top_search_book,width=25,height=15,font=('Arial',15,'italic','bold'))
    Search_book_Book_name.grid(row=1,column=2,pady=30,padx=20)
    Search_book_Or=Label(Top_search_book,text='Or',font=('Arial',27,'bold'),bg='white',fg='red')
    Search_book_Or.grid(row=2,column=1,pady=30,padx=20)
    Search_book_Book_serial_no_heading=Label(Top_search_book,text='Book Serial No',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Book_serial_no_heading.grid(row=3,column=1,pady=30,padx=20)
    Search_book_Book_serial_no=ttk.Combobox(Top_search_book,width=25,height=15,font=('Arial',15,'italic','bold'))
    Search_book_Book_serial_no.grid(row=3,column=2,pady=30,padx=20)
    Search_book_Search_button=Button(Top_search_book,text='Search',font=('Arial',30,'italic'),fg='white',bg='black',command=Search_book_execution)
    Search_book_Search_button.grid(row=4,column=2,pady=30,padx=20)
    loaddatabooks(Search_book_Book_name)
    loadserialbooks(Search_book_Book_serial_no)
    Search_book_Display_book_serial_no_heading=Label(Top_search_book,text='Book Serial No',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Display_book_serial_no_heading.grid(row=5,column=0,pady=30,padx=20)
    Search_book_Display_book_serial_no=Text(Top_search_book,width=28,height=2.5,bg='cyan',font=25)
    Search_book_Display_book_serial_no.grid(row=6,column=0,pady=30,padx=20)
    Search_book_Display_book_name_heading=Label(Top_search_book,text='Book Name',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Display_book_name_heading.grid(row=5,column=1,pady=30,padx=20)
    Search_book_Display_book_name=Text(Top_search_book,width=28,height=2.5,bg='cyan',font=25)
    Search_book_Display_book_name.grid(row=6,column=1,pady=30,padx=20)
    Search_book_Display_price_heading=Label(Top_search_book,text='Price',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Display_price_heading.grid(row=5,column=2,pady=30,padx=20)
    Search_book_Display_price=Text(Top_search_book,width=28,height=2.5,bg='cyan',font=25)
    Search_book_Display_price.grid(row=6,column=2,pady=30,padx=20)
    Search_book_Display_status_heading=Label(Top_search_book,text='Status',font=('Arial',27,'bold'),bg='white',fg='black')
    Search_book_Display_status_heading.grid(row=5,column=3,pady=30,padx=20)
    Search_book_Display_status=Text(Top_search_book,width=28,height=2.5,bg='cyan',font=25)
    Search_book_Display_status.grid(row=6,column=3,pady=30,padx=20)
    Search_book_Refresh_button=Button(Top_search_book,text="Refresh",bg='lawn green',fg='black',font=('Arial',25,'bold'),command=Refresh_search_book)
    Search_book_Refresh_button.grid(row=6,column=4,pady=30,padx=20)
    Search_book_Back_button=Button(Top_search_book,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_search_book.destroy)
    Search_book_Back_button.place(x=1350,y=800)

def Remove_student_execution():
    global Remove_student_Roll_no
    cur=db.cursor()
    Remove_student_execution_roll_no=Remove_student_Roll_no.get()
    sql1="select Srbook from assignment where Rstudent="+str(Remove_student_execution_roll_no)
    cur.execute(sql1)
    rs=cur.fetchone()
    if(rs!=None):
        Remove_student_execution_update=rs[0]
        sql2="delete from assignment where Rstudent="+str(Remove_student_execution_roll_no)
        cur.execute(sql2)
        sql3="update books set Status='Available' where Sr_no="+str(Remove_student_execution_update)
        cur.execute(sql3)
        data1=(Remove_student_execution_update,Remove_student_execution_roll_no)
        sql4="update display set Student_status='No longer student' where Serial_bookno=%s and Student_rollno=%s"
        cur.execute(sql4,data1)
        db.commit()
    sql5="delete from students where Roll_no="+str(Remove_student_execution_roll_no)
    cur.execute(sql5)
    messagebox.showinfo("Removed","Student Removed Successfully")
    

def Remove_student():
    global Remove_student_Roll_no
    Top_remove_student=Toplevel(root)
    Top_remove_student.geometry("1500x1500")
    Top_remove_student.title("Remove a Student")
    Remove_student_Roll_no_heading=Label(Top_remove_student,text='Roll Number',font=('Arial',27,'bold'),bg='white',fg='black')
    Remove_student_Roll_no_heading.grid(row=1,column=1,pady=30)
    Remove_student_Roll_no=ttk.Combobox(Top_remove_student,width=25,height=15,font=('Arial',15,'italic','bold'))
    Remove_student_Roll_no.grid(row=1,column=3,pady=30)
    loadserialstudents(Remove_student_Roll_no)
    Remove_student_Remove_button=Button(Top_remove_student,text='Remove',font=('Arial',30,'italic'),fg='white',bg='black',command=Remove_student_execution)
    Remove_student_Remove_button.grid(row=3,column=2,pady=30)
    Remove_student_Back_button=Button(Top_remove_student,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_remove_student.destroy)
    Remove_student_Back_button.place(x=1350,y=800)

def Remove_book_execution():
    global Remove__book_Book_serial_no
    cur=db.cursor()
    Remove_book_execution_book_serial_no=Remove__book_Book_serial_no.get()
    sql1="delete from assignment where Srbook="+str(Remove_book_execution_book_serial_no)
    cur.execute(sql1)
    sql2="delete from books where Sr_no="+str(Remove_book_execution_book_serial_no)
    cur.execute(sql2)
    db.commit()
    messagebox.showinfo("Removed","Book Removed Successfully")

def Remove_book():
    global Remove__book_Book_serial_no
    Top_remove_book=Toplevel(root)
    Top_remove_book.geometry("1500x1500")
    Top_remove_book.title("Remove a Book")
    Remove__book_Book_serial_no_heading=Label(Top_remove_book,text='Serial Number',font=('Arial',27,'bold'),bg='white',fg='black')
    Remove__book_Book_serial_no_heading.grid(row=1,column=1,pady=30)
    Remove__book_Book_serial_no=ttk.Combobox(Top_remove_book,width=25,height=15,font=('Arial',15,'italic','bold'))
    Remove__book_Book_serial_no.grid(row=1,column=3,pady=30)
    Remove__book_Remove_button=Button(Top_remove_book,text='Remove',font=('Arial',30,'italic'),fg='white',bg='black',command=Remove_book_execution)
    Remove__book_Remove_button.grid(row=3,column=2,pady=30)
    loadserialbooks(Remove__book_Book_serial_no)
    Remove__book_Back_button=Button(Top_remove_book,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_remove_book.destroy)
    Remove__book_Back_button.place(x=1350,y=800)

def Assign_book_execution():
    global Assign_book_Book_serial_no,Assign_book_Roll_no
    Assign_book_execution_book_serial_no=Assign_book_Book_serial_no.get()
    Assign_book_execution_roll_no=Assign_book_Roll_no.get()
    Assign_book_execution_today_date=date.today()
    cur=db.cursor()
    sql1="select Status from books where Sr_no="+str(Assign_book_execution_book_serial_no)
    cur.execute(sql1)
    check=cur.fetchone()
    check=check[0]
    if(check=='Not Available'):
        messagebox.showinfo("Not Available","Currently book is not available")
    else:
        sql2="insert into assignment values(%s,%s,%s,%s,%s)"
        data2=(Assign_book_execution_book_serial_no,Assign_book_execution_roll_no,Assign_book_execution_today_date,0000-00-00,0)
        cur.execute(sql2,data2)
        sql3="update books set Status='Not Available' where Sr_no="+str(Assign_book_execution_book_serial_no)
        cur.execute(sql3)
        sql4="insert into display values(%s,%s,%s,%s,%s,%s)"
        data4=(Assign_book_execution_book_serial_no,Assign_book_execution_roll_no,Assign_book_execution_today_date,0000-00-00,0,'Student')
        cur.execute(sql4,data4)
        messagebox.showinfo("Assigned","Book Assigned")
    db.commit()

def Assign_book():
    global Assign_book_Book_serial_no,Assign_book_Roll_no
    Top_Assign_book=Toplevel(root)
    Top_Assign_book.geometry('1500x1500')
    Top_Assign_book.title("Let's Assign")
    Assign_book_Book_serial_no_heading=Label(Top_Assign_book,text="Book's Serial NO",font=('Arial',27,'bold'),bg='white',fg='black')
    Assign_book_Book_serial_no_heading.grid(row=5,column=1,pady=10)
    Assign_book_Book_serial_no=ttk.Combobox(Top_Assign_book,width=25,height=15,font=('Arial',15,'italic','bold'))
    Assign_book_Book_serial_no.grid(row=5,column=3,pady=30)
    loadserialbooks(Assign_book_Book_serial_no)
    Assign_book_Roll_no_heading=Label(Top_Assign_book,text='Roll Number',font=('Arial',30,'bold'),bg='white',fg='black')
    Assign_book_Roll_no_heading.grid(row=6,column=1,pady=30)
    Assign_book_Roll_no=ttk.Combobox(Top_Assign_book,width=25,height=15,font=('Arial',15,'italic','bold'))
    Assign_book_Roll_no.grid(row=6,column=3,pady=30)
    loadserialstudents(Assign_book_Roll_no)
    Assign_book_Assign_button=Button(Top_Assign_book,text='Assign',font=('Arial',30,'italic'),fg='white',bg='black',command=Assign_book_execution)
    Assign_book_Assign_button.grid(row=8,column=2,pady=30)
    Assign_book_Back_button=Button(Top_Assign_book,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_Assign_book.destroy)
    Assign_book_Back_button.place(x=1350,y=800)

def Display_students():
    Top_display_students=Toplevel(root)
    Top_display_students.geometry('1500x1500')
    Top_display_students.title("Display all student")
    Display_studentscmb1=ttk.Combobox(Top_display_students,width=35,height=35,font=('Arial',25,'italic','bold'))
    Display_studentscmb1.grid(row=2,column=1,padx=20)
    loaddatastudents(Display_studentscmb1)
    Display_studentsBack_button=Button(Top_display_students,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_display_students.destroy)
    Display_studentsBack_button.place(x=1350,y=800)

def Display_books():
    Top_display_books=Toplevel(root)
    Top_display_books.geometry('1500x1500')
    Top_display_books.title("Display all Books")
    Display_books_cmb1=ttk.Combobox(Top_display_books,width=35,height=35,font=('Arial',25,'italic','bold'))
    Display_books_cmb1.grid(row=2,column=1,padx=20)
    loaddatabooks(Display_books_cmb1)
    Display_books_Back_button=Button(Top_display_books,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_display_books.destroy)
    Display_books_Back_button.place(x=1350,y=800)

def Add_student_execution():
    global Add_student_Roll_no,Add_student_Student_name,Add_student_Branch
    cur=db.cursor()
    Add_student_execution_roll_no=Add_student_Roll_no.get("1.0","end-1c")
    Add_student_execution_name=Add_student_Student_name.get("1.0","end-1c")
    Add_student_execution_branch=Add_student_Branch.get("1.0","end-1c")
    sql="insert into students(Roll_no,Sname,Branch) values(%s,%s,%s)"
    data=(Add_student_execution_roll_no,Add_student_execution_name,Add_student_execution_branch)
    cur.execute(sql,data)
    db.commit()
    Add_student_Roll_no.delete("1.0","end")
    Add_student_Student_name.delete("1.0","end")
    Add_student_Branch.delete("1.0","end")
    messagebox.showinfo("Added","Student Added Successfully")


def Add_student():
    global Add_student_Roll_no,Add_student_Student_name,Add_student_Branch
    Top_add_student=Toplevel(root)
    Top_add_student.geometry('1500x1500')
    Top_add_student.title("Add a Student")
    Add_student_Roll_no_heading=Label(Top_add_student,text='Roll No',font=('Arial',27,'bold'),bg='white',fg='black')
    Add_student_Roll_no_heading.grid(row=1,column=1,pady=20)
    Add_student_Roll_no=Text(Top_add_student,width=28,height=2.5,bg='cyan',font=25)
    Add_student_Roll_no.grid(row=1,column=3,pady=20)
    Add_student_Student_name_heading=Label(Top_add_student,text='Student Name',font=('Arial',30,'bold'),bg='white',fg='black')
    Add_student_Student_name_heading.grid(row=2,column=1,pady=20)
    Add_student_Student_name=Text(Top_add_student,width=28,height=2.5,bg='cyan',font=25)
    Add_student_Student_name.grid(row=2,column=3,pady=20)
    Add_student_Branch_heading=Label(Top_add_student,text='Branch',font=('Arial',30,'bold'),bg='white',fg='black')
    Add_student_Branch_heading.grid(row=3,column=1,pady=20)
    Add_student_Branch=Text(Top_add_student,width=28,height=2.5,bg='cyan',font=25)
    Add_student_Branch.grid(row=3,column=3,pady=20)
    Add_student_Add_button=Button(Top_add_student,text='Add',font=('Arial',30,'italic'),fg='white',bg='black',command=Add_student_execution)
    Add_student_Add_button.grid(row=4,column=2,pady=20)
    Add_student_Back_button=Button(Top_add_student,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_add_student.destroy)
    Add_student_Back_button.place(x=1350,y=800)

def Add_book_execution():
    global Add_book_Book_name,Add_book_Price
    cur=db.cursor()
    Add_book_execution_book_name=Add_book_Book_name.get("1.0","end-1c")
    Add_book_execution_price=Add_book_Price.get("1.0","end-1c")
    sql="insert into books(Bookname,Price,Status) values(%s,%s,%s)"
    data=(Add_book_execution_book_name,Add_book_execution_price,'Available')
    cur.execute(sql,data)
    db.commit()
    Add_book_Book_name.delete("1.0","end")
    Add_book_Price.delete("1.0","end")
    messagebox.showinfo("Added","Book Added Successfully")

def Add_book():
    global Add_book_Book_name,Add_book_Price
    Top_add_book=Toplevel(root)
    Top_add_book.geometry('1500x1500')
    Top_add_book.title("Add a book")
    Add_book_Book_name_heading=Label(Top_add_book,text='Book Name',font=('Arial',27,'bold'),bg='white',fg='black')
    Add_book_Book_name_heading.grid(row=5,column=1,pady=30)
    Add_book_Book_name=Text(Top_add_book,width=28,height=2.5,bg='cyan',font=25)
    Add_book_Book_name.grid(row=5,column=3,pady=30)
    Add_book_Price_heading=Label(Top_add_book,text='Price',font=('Arial',30,'bold'),bg='white',fg='black')
    Add_book_Price_heading.grid(row=6,column=1,pady=30)
    Add_book_Price=Text(Top_add_book,width=28,height=2.5,bg='cyan',font=25)
    Add_book_Price.grid(row=6,column=3,pady=30)
    Add_book_Add_button=Button(Top_add_book,text='Add',font=('Arial',30,'italic','bold'),fg='white',bg='black',command=Add_book_execution)
    Add_book_Add_button.grid(row=7,column=2,pady=30)
    Add_book_Back_button=Button(Top_add_book,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_add_book.destroy)
    Add_book_Back_button.place(x=1350,y=800)

def Options():
    Top_options=Toplevel(root)
    Top_options.title("Select an option")
    Top_options.geometry("1500x1500")
    Options_Label_option=Label(Top_options,text="------: Select an option :-----",fg='red',font=('Algerian',40,"italic"))
    Options_Label_option.grid(row=0,column=2,pady=25)
    Options_Add_books_button=Button(Top_options,text='ADD A BOOK',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Add_book)
    Options_Add_books_button.grid(row=1,column=0,pady=25)
    Options_Add_student_button=Button(Top_options,text='ADD A STUDENT',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Add_student)
    Options_Add_student_button.grid(row=1,column=4,pady=25)
    Options_Display_books_button=Button(Top_options,text='DISPLAY BOOKS',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Display_books)
    Options_Display_books_button.grid(row=2,column=0,pady=25)
    Options_Display_students_button=Button(Top_options,text='DISPLAY STUDENTS',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Display_students)
    Options_Display_students_button.grid(row=2,column=4,pady=25)
    Options_Assign_book_button=Button(Top_options,text='ASSIGN A BOOK',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Assign_book)
    Options_Assign_book_button.grid(row=3,column=0,pady=25)
    Options_Remove_book_button=Button(Top_options,text='REMOVE A BOOK',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Remove_book)
    Options_Remove_book_button.grid(row=4,column=0,pady=25)
    Options_Remove_student_button=Button(Top_options,text='REMOVE A STUDENT',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Remove_student)
    Options_Remove_student_button.grid(row=4,column=4,pady=25)
    Options_Search_book_button=Button(Top_options,text='SEARCH A BOOK',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Search_book)
    Options_Search_book_button.grid(row=5,column=0,pady=25)
    Options_Search_student_button=Button(Top_options,text='SEARCH A STUDENT',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Search_student)
    Options_Search_student_button.grid(row=5,column=4,pady=25)
    Options_Submit_book_button=Button(Top_options,text='SUBMIT A BOOK',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Submit)
    Options_Submit_book_button.grid(row=3,column=4,pady=25)
    Options_Display_assigned_books_button=Button(Top_options,text='Display Assigned Books',fg='black',bg='medium spring green',font=("Arial",20,"bold"),command=Display_assign)
    Options_Display_assigned_books_button.grid(row=6,column=0,pady=25)
    Options_Back_button=Button(Top_options,text="Back",bg='orange',fg='black',font=('Arial',15,'bold'),command=Top_options.destroy)
    Options_Back_button.grid(row=6,column=4,pady=35)

def Verification():
    username=Username.get("1.0","end-1c")
    password=Password.get("1.0","end-1c")
    login_username='123'
    login_password='123'
    if(login_username==username and login_password==password):
        Options()
    else:
        messagebox.showwarning('Invalid User','Wrong password or username')

root=Tk()
root.geometry("1000x500")
root.title("Kendriya Vidyalaya No.1 Sagar")
Welcome=Label(root,text="Welcome to Library",font=('Arial',55,'italic'),fg='black')
Welcome.grid(row=0,column=1)
Username_heading=Label(root,text='Username',font=("Arial",40,"bold"))
Username_heading.grid(row=1,column=0,pady=25)
Username=Text(width=28,height=3,bg='cyan',font=25)
Username.grid(row=1,column=1)
Password_heading=Label(root,text='Password',font=("Arial",40,"bold"))
Password_heading.grid(row=3,column=0)
Password=Text(width=28,height=3,bg='cyan',font=25)
Password.grid(row=3,column=1)
Login_button=Button(root,text="Login",font=("Arial",20,"bold"),fg='white',bg='black',command=Verification)
Login_button.grid(row=4,column=1,pady=25)
Exit_button=Button(root,text="Exit",bg='white',fg='red',font=('Arial',15,'bold'),command=root.destroy)
Exit_button.grid(row=5,column=2)
root.mainloop()