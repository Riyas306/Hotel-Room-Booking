import MySQLdb
db=MySQLdb.connect('localhost','root','*****','student')
c=db.cursor()
from Tkinter import *
import tkMessageBox
t=Tk()
def registration():
    sql="""insert into booking(Name,Address,Id,User_Name,Password) values('%s','%s','%d','%s','%d')"""
    %(str(name.get()),str(address.get()),int(idn.get()),str(uname.get()),int(pswd.get()))
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()
    name.delete(0,END)
    address.delete(0,END)
    
    idn.delete(0,END)
    uname.delete(0,END)
    pswd.delete(0,END)
    tkMessageBox.showinfo(message="registration complete")

def page():
    t2=Tk()
    Label(t2,text="Username",relief=RAISED).grid(row=8,column=0)
    Label(t2,text="Password",relief=RAISED).grid(row=9,column=0)
    uname=Entry(t2)
    pswd=Entry(t2,show='*')
    uname.grid(row=8,column=1)
    pswd.grid(row=9,column=1)
    def check():
        
        sql="""select Password from booking where User_Name='%s'"""%(str(uname.get()))
        
        try:
            c.execute(sql)
            result=c.fetchone()
            for i in result:
                if (result[0]==123456789):
                    def acroom():
                        s="""select * from room where type='A/C'"""
                        try:
                            c.execute(s)
                            a=c.fetchall()
                            for i in a:
                                b="Room no='%d'\nStatus='%s'\nRent='%d'\nType='%s'"%(i[0],i[1],i[2],i[3])
                                tkMessageBox.showinfo(title="ac",message=b)
                            db.commit()
                        except Exception,e:
                            print e
                            db.rollback()
                    
                    def nonacroom():
                        n="""select * from room where type='NON A/C'"""
                        try:
                            c.execute(n)
                            b=c.fetchall()
                            for i in b:
                                d="Room no='%d'\nStatus='%s'\nRent='%d'\nType='%s'\nview='%s'"%(i[0],i[1],i[2],i[3],i[4])
                                tkMessageBox.showinfo(title="nonac",message=d)
                            db.commit()
                        except Exception,e:
                            print e
                            db.rollback()
                            
                    def add():
                        t4=Tk()
                        Label(t4,text="Roomno").grid(row=1)
                        Label(t4,text="Status").grid(row=2)
                        Label(t4,text="Rent").grid(row=3)
                        Label(t4,text="Type").grid(row=4)
                        e1=Entry(t4)
                        e2=Entry(t4)
                        e3=Entry(t4)
                        e4=Entry(t4)
                        e1.grid(row=1,column=1)
                        e2.grid(row=2,column=1)
                        e3.grid(row=3,column=1)
                        e4.grid(row=4,column=1)
                        def add1():
                            sql="insert into room(roomno,status,rent,type,view)values('%d','%s','%d','%s','%s')"%(int(e1.get()),str(e2.get()),int(e3.get()),str(e4.get()),"free")
                            try:
                                c.execute(sql)
                                db.commit()
                                e1.delete(0,END)
                                e2.delete(0,END)
                                e3.delete(0,END)
                                e4.delete(0,END)
                            except:
                                db.rollback()
                        add2=Button(t4,text="ADD",relief=RAISED,command=add1)
                        add2.grid(row=5,column=1)
                    def remove():
                        t4=Tk()
                        Label(t4,text="Room no").grid()
                        ee=Entry(t4)
                        ee.grid(column=1)
                        def remove1():
                            s="delete from room where roomno='%d'"%(int(ee.get()))
                            try:
                                c.execute(s)
                                db.commit()
                                ee.delete(0,END)
                            except:
                                db.rollback()
                        remv=Button(t4,text="REMOVE",command=remove1)
                        remv.grid(column=1)
                    def mngmnt():
                        t4=Tk()
                        def check_in():
                            sql="insert into reports(roomno)values('%d')"%(int(r.get()))
                            t="select current_date()"
                            try:
                                c.execute(sql)
                                c.execute(t)
                                result=c.fetchone()
                                for i in result:
                                    c.execute("update reports set check_in='%s' where roomno='%d'"%(i,int(r.get())))
                                    db.commit()
                            except Exception,e:
                                
                                print e
                                db.rollback()
                            tkMessageBox.showinfo(message="check_in complete")
                        def check_out():
                            
                            sql="select current_date()"
                            try:
                                c.execute(sql)
                                result=c.fetchone()
                                for i in result:
                                    c.execute("update reports set check_out='%s' where roomno='%d'"%(i,int(r1.get())))
                                    
                                c.execute("select Id from managment where roomno='%d'"%(int(r1.get())))
                                i=c.fetchone()
                                db.commit()
                                
                            except Exception,e:
                                print e
                                db.rollback()
                            tkMessageBox.showinfo(message="check_out complete")
                            try:
                                c.execute("select Name,Address,Id from booking where Id='%d'"%(int(i1.get())))
                                result=c.fetchall()
                                for i in result:
                                    c.execute("insert into bills(Name,Address,Id,amount,roomno)values('%s','%s','%d','%d','%d')"%(str(i[0]),str(i[1]),int(i[2]),int(a.get()),int(r1.get())))
                                
                                c.execute("select * from reports")
                                rp=c.fetchall()
                                for i in rp:
                                    c.execute("update bills set check_in='%s' where id='%d'"%(i[1],int(i1.get())))
                                    c.execute("update bills set check_out='%s' where id='%d'"%(i[2],int(i1.get())))
                                db.commit()
                            except Exception,e:
                                print e
                                db.rollback()

                            try:
                                c.execute("update room set view='%s' where roomno='%d'"%("free",int(r1.get())))
                                c.execute("delete from managment where roomno='%d'"%(int(r1.get())))
                                
                                db.commit()
                                
                            except Exception,e:
                                print e
                                db.rollback()
                            try:
                                c.execute("select * from bills")
                                result=c.fetchall()
                                for i in result:
                                    d="Name='%s'\nAddress='%s'\nId='%s'\namount='%d'\nroomno='%d'\ncheck_in='%s'\ncheck_out='%s'"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                                tkMessageBox.showinfo(title="bill",message=d)
                                db.commit()
                            except Exception,e:
                                print e
                                db.rollback()
                        sql="select * from room natural join managment"
                        try:
                            c.execute(sql)
                            result=c.fetchall()
                            for i in result:
                                d="roomno='%d',view='%s',status='%s',rent='%d',type='%s',Id='%d'"%(i[0],i[1],i[2],i[3],i[4],i[5])
                                l=Listbox(t4,selectmode=SINGLE)
                                l.grid(row=8)
                                l.insert(1,d)
                        except Exception,e:
                            print e
                            db.rollback()
                            
                        Label(t4,text="BOOKING MANAGMENT",bg="red",fg="blue",relief=RAISED).grid(column=1)
                        Label(t4,text="Enter Id",relief=RAISED).grid(row=1)
                        i=Entry(t4)
                        i.grid(row=1,column=1)
                        Label(t4,text="Room no",relief=RAISED).grid(row=2)
                        r=Entry(t4)
                        r.grid(row=2,column=1)
                        ci=Button(t4,text="CHECK IN",relief=RAISED,command=check_in)
                        ci.grid(row=4,column=1)
                        
                        Label(t4,text="Room no for check out",relief=RAISED).grid(row=5)
                        r1=Entry(t4)
                        r1.grid(row=5,column=1)
                        Label(t4,text="Id for check out",relief=RAISED).grid(row=6)
                        i1=Entry(t4)
                        i1.grid(row=6,column=1)
                        Label(t4,text="enter amount",relief=RAISED).grid(row=7)
                        a=Entry(t4)
                        a.grid(row=7,column=1)
                        co=Button(t4,text="CHECK OUT",relief=RAISED,command=check_out)
                        co.grid(row=8,column=1)
                        
                            
                        
                    def edt():
                        t4=Tk()
                        Label(t4,text="User_Name",relie=RAISED).grid()
                        Label(t4,text="Password",relie=RAISED).grid(row=1)
                        Label(t4,text="New User_Name",relie=RAISED).grid(row=2)
                        Label(t4,text="New Password",relie=RAISED).grid(row=3)
                        usr=Entry(t4)
                        pwd=Entry(t4)
                        nusr=Entry(t4)
                        npwd=Entry(t4)
                        usr.grid(row=0,column=1)
                        pwd.grid(row=1,column=1)
                        nusr.grid(row=2,column=1)
                        npwd.grid(row=3,column=1)
                        sbmt=Button(t4,text="SUBMIT",bg="blue",relief=RAISED).grid(row=4,column=1)
                    
                        

                    t3=Tk()
                    Label(t3,text="ROOM DETAILS",bg="blue",relief=RAISED).grid(row=0,column=1)
                    Label(t3,text="ROOM TYPE").grid(row=1,column=1)
                    ac=Button(t3,text="A/C",relief=RAISED,command=acroom)
                    ac.grid(row=2)
                    nonac=Button(t3,text="NON A/C",relief=RAISED,command=nonacroom)
                    nonac.grid(row=2,column=2)
                    add=Button(t3,text="ADD ROOM",relief=RAISED,command=add)
                    add.grid(row=4)
                    delete=Button(t3,text="REMOVE ROOM",relief=RAISED,command=remove)
                    delete.grid(row=5)
                    managment=Button(t3,text="BOOKING MANAGMENT",relief=RAISED,command=mngmnt)
                    managment.grid(row=5,column=1)
                    edit=Button(t3,text="Edit User name and Password",relief=RAISED,command=edt)
                    edit.grid(row=6)
                    rprt=Button(t3,text="REPORTS",relief=RAISED,command=reports)
                    rprt.grid(row=7)
                    
                
                elif (int(pswd.get())==result[0]):
                    t5=Tk()
                    def book():
                        
                        s="select Id from booking where User_Name='%s'"%(str(uname.get()))
                        sql="update room set view='%s' where roomno='%d'"%("BOOKED",int(r.get()))
                        try:
                            c.execute(s)
                            
                            result=c.fetchone()
                            c.execute("select roomno from room")
                            d=c.fetchall()
                            l=[int(i[0]) for i in d if i>99]
                            if int(r.get()) in l:
                                c.execute("insert into managment(roomno,view,Id)values('%d','%s','%d')"%(int(r.get()),"Booked",int(result[0])))
                            
                            else:
                                tkMessageBox.showinfo(message="invalid room no")
                            c.execute(sql)    
                            db.commit()   
                        except Exception,e:
                            print e
                            db.rollback()
                        tkMessageBox.showinfo(message="booking complete")
                    sql="select * from room"
                    try:
                        c.execute(sql)
                        result=c.fetchall()
                        for i in result:
                            d="Room no='%d'\nStatus='%s'\nRent='%d'\nType='%s'\nview='%s'"%(i[0],i[1],i[2],i[3],i[4])
                            tkMessageBox.showinfo(title="room",message=d)
                            db.commit()
                    except Exception,e:
                        print e
                        db.rollback()
                    Label(t5,text="WELCOME",bg="red",fg="black",relief=RAISED).grid(column=1)
                    
                    Label(t5,text="enter room no",relief=RAISED).grid(row=2)
                    r=Entry(t5)
                    r.grid(row=2,column=1)
                    book=Button(t5,text="BOOK",relief=RAISED,command=book)
                    book.grid(row=3,column=1)
                    
                else:
                    tkMessageBox.showinfo(title="error",message="invalid Password or User Name")
            db.commit()
            
        except:
            db.rollback()
    login2=Button(t2,text="LOGIN",bg="blue",relief=RAISED,command=check)
    login2.grid(row=10,column=1)
    

Label(t,text="REGISTRATION FORM",relief=RAISED,bg="red",fg="black",padx=10,bd=5).grid(row=0,column=1)
Label(t,text="Name",relief=RAISED).grid(row=1,column=0)
Label(t,text="Address",relief=RAISED,width=10).grid(row=2,column=0)
Label(t,text="Idnumber",relief=RAISED).grid(row=3,column=0)
Label(t,text="Username",relief=RAISED).grid(row=4,column=0)
Label(t,text="Password",relief=RAISED).grid(row=5,column=0)
name=Entry(t)
address=Entry(t)
idn=Entry(t)
uname=Entry(t)
pswd=Entry(t,show='*')
name.grid(row=1,column=1)
address.grid(row=2,column=1)
idn.grid(row=3,column=1)
uname.grid(row=4,column=1)
pswd.grid(row=5,column=1)
signup=Button(t,text="SIGNUP",bg="blue",relief=RAISED,command=registration).grid(row=6,column=0)
login=Button(t,text="LOGIN",bg="blue",relief=RAISED,command=page).grid(row=6,column=2)

t.mainloop()

