from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time

class Customer():
    def __init__(self,root):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1370x640+0+0")
        self.root.config(bg="#F5D020")

            ###############-----------FRAMES----------################

        f = Frame(self.root,bg="#F5D020", bd=20,relief=RIDGE)
        f.grid()
        f1 = Frame(f,bd=14,width=1350, height=300, padx=10, bg="#F5D020",relief=RIDGE)
        f1.grid(row=0,column=0,columnspan=4,sticky='W')
        f2 = Frame(f,bd=14,width=460, height=488, padx=10, bg="#8703D0",relief=RIDGE)
        f2.grid(row=1,column=0,sticky='w')
        f3 = Frame(f,bd=14,width=460, height=488, padx=10, bg="#F5D020",relief=RIDGE)
        f3.grid(row=1,column=1,sticky='w')
        f4 = Frame(f,bd=14,width=470, height=488, padx=10, bg="#8703D0",relief=RIDGE)
        f4.grid(row=1,column=2,sticky='w')
        f5 = Frame(f4,bd=14,width=380, height=340, padx=10, bg="#8703D0",relief=RIDGE)
        f5.grid(row=0,column=0,sticky='w')
        f6 = Frame(f4,bd=14,width=380, height=120, padx=10, bg="#8703D0",relief=RIDGE)
        f6.grid(row=1,column=0,columnspan=4,sticky='W')



        Date1=StringVar()
        Time1=StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H.%M.%S"))

        self.lblTitle=Label(f1,textvariable=Date1,font=('arial',30,'bold'),pady=9,
                            bd=5,bg="#8703D0",fg="Cornsilk").grid(row=0,column=0)

        self.lblTitle=Label(f1,text="\tCustomer Billing System\t\t",font=('arial',30,'bold'),pady=9,
                            bd=5,bg="#8703D0",fg="Cornsilk",justify='center').grid(row=0,column=1)

        self.lblTitle=Label(f1,textvariable=Time1,font=('arial',30,'bold'),pady=9,
                            bd=5,bg="#8703D0",fg="Cornsilk").grid(row=0,column=2)

        #############-------------------Variables------------###################


        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        Paidtax = StringVar()
        TotalDays = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        ##########---------------Setting Random CustomerRef------------#########

        CustomerRef.set(random.randint(1000,10000))

        ##########--------------Variables For CheckButton----------#############

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        Coffee=StringVar()
        Tea=StringVar()
        Juice=StringVar()
        Milk=StringVar()
        ColdDrink=StringVar()
        Omlette=StringVar()
        BreadButter=StringVar()
        Salad=StringVar()

        Coffee.set("0")
        Tea.set("0")
        Juice.set("0")
        Milk.set("0")
        ColdDrink.set("0")
        Omlette.set("0")
        BreadButter.set("0")
        Salad.set("0")



            ####################--------Exit Function--------###################

        def Exit():
            exit = tkinter.messagebox.askyesno("Computer Billing System","Confirm if you want to exit")
            if exit>0:
                root.destroy()
                return


            #######################-----Reset Function-----#####################

        def Reset():
                            #####---Reset For Text Recipt---#####
            self.txtReciept.delete("1.0",END)

                            #####---Reset For I/p values---#####
            Coffee.set("0")
            Tea.set("0")
            Juice.set("0")
            Milk.set("0")
            ColdDrink.set("0")
            Omlette.set("0")
            BreadButter.set("0")
            Salad.set("0")

            CustomerRef.set(random.randint(1000,10000))
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")


                #####---Reset For CheckButton---#####


            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

    ###########-------Function for enable/disable CheckButton------#############

        def chkCoffee():
            if var1.get() == 1:
                self.txtCoffee.configure(state='normal')
                self.txtCoffee.focus()
                self.txtCoffee.delete(0,END)
            elif var1.get() == 0:
                self.txtCoffee.configure(state='disabled')


        def chkTea():
            if var2.get() == 1:
                self.txtTea.configure(state='normal')
                self.txtTea.focus()
                self.txtTea.delete(0,END)
            elif var2.get() == 0:
                self.txtTea.configure(state='disabled')

        def chkJuice():
            if var3.get() == 1:
                self.txtJuice.configure(state='normal')
                self.txtJuice.focus()
                self.txtJuice.delete(0,END)
            elif var3.get() == 0:
                self.txtJuice.configure(state='disabled')

        def chkMilk():
            if var4.get() == 1:
                self.txtMilk.configure(state='normal')
                self.txtMilk.focus()
                self.txtMilk.delete(0,END)
            elif var4.get() == 0:
                self.txtMilk.configure(state='disabled')

        def chkColdDrink():
            if var5.get() == 1:
                self.txtColdDrink.configure(state='normal')
                self.txtColdDrink.focus()
                self.txtColdDrink.delete(0,END)
            elif var5.get() == 0:
                self.txtColdDrink.configure(state='disabled')

        def chkOmlette():
            if var6.get() == 1:
                self.txtOmlette.configure(state='normal')
                self.txtOmlette.focus()
                self.txtOmlette.delete(0,END)
            elif var6.get() == 0:
                self.txtOmlette.configure(state='disabled')

        def chkBreadButter():
            if var7.get() == 1:
                self.txtBreadButter.configure(state='normal')
                self.txtBreadButter.focus()
                self.txtBreadButter.delete(0,END)
            elif var7.get() == 0:
                self.txtBreadButter.configure(state='disabled')

        def chkSalad():
            if var8.get() == 1:
                self.txtSalad.configure(state='normal')
                self.txtSalad.focus()
                self.txtSalad.delete(0,END)
            elif var8.get() == 0:
                self.txtSalad.configure(state='disabled')


    ##############-------Function for calculating Total Amount-----#############


        def Total():
            item1=float(Coffee.get())
            item2=float(Tea.get())
            item3=float(Juice.get())
            item4=float(Milk.get())
            item5=float(ColdDrink.get())
            item6=float(Omlette.get())
            item7=float(BreadButter.get())
            item8=float(Salad.get())

            sumcost = ((item1*25)+(item2*10)+(item3*35)+(item4*45)+
                        (item5*40)+(item6*70)+(item7*35)+(item8*50))

            PaidTax.set(sumcost * .15)
            SubTotal.set(sumcost)
            TotalCost.set(float(PaidTax.get()) + float(SubTotal.get()))

        ##################-------Printing on TextBox------##################

            self.txtReciept.delete('1.0',END)
            self.txtReciept.insert(END,f'\nCoffee\t\t\t\t\t {self.txtCoffee.get()}')
            self.txtReciept.insert(END,f'\nTea\t\t\t\t\t {self.txtTea.get()}')
            self.txtReciept.insert(END,f'\nJuice\t\t\t\t\t {self.txtJuice.get()}')
            self.txtReciept.insert(END,f'\nMilk\t\t\t\t\t {self.txtMilk.get()}')
            self.txtReciept.insert(END,f'\nColdDrink\t\t\t\t\t {self.txtColdDrink.get()}')
            self.txtReciept.insert(END,f'\nOmlette\t\t\t\t\t {self.txtOmlette.get()}')
            self.txtReciept.insert(END,f'\nBreadButter\t\t\t\t\t {self.txtBreadButter.get()}')
            self.txtReciept.insert(END,f'\n\n----------------------------------------------')
            self.txtReciept.insert(END,f'\n\nSubTotal\t\t\t\t Rs. {SubTotal.get()}')
            self.txtReciept.insert(END,f'\nTaxPaid\t\t\t\t Rs. {PaidTax.get()}')
            self.txtReciept.insert(END,f'\n\nTotalBill\t\t\t\t Rs. {TotalCost.get()}')



                ##################----Text Box For Recipt----###################

        self.txtReciept = Text(f5, height=19, width=43, bd=10, font=('arial',9,'bold'))
        self.txtReciept.grid(row=0,column=0)

            ################-------CheckButton & Entry--------##################

        self.Coffee=Checkbutton(f3, text="Coffee",variable=var1,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkCoffee)
        self.Coffee.grid(row=0,sticky='w')
        self.txtCoffee=Entry(f3,font=('arial',12,'bold'),textvariable=Coffee,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtCoffee.grid(row=0,column=1)

        self.Tea=Checkbutton(f3, text="Tea",variable=var2,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkTea)
        self.Tea.grid(row=1,sticky='w')
        self.txtTea=Entry(f3,font=('arial',12,'bold'),textvariable=Tea,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtTea.grid(row=1,column=1)

        self.Juice=Checkbutton(f3, text="Juice",variable=var3,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkJuice).grid(row=2,sticky='w')
        self.txtJuice=Entry(f3,font=('arial',12,'bold'),textvariable=Juice,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtJuice.grid(row=2,column=1)

        self.Milk=Checkbutton(f3, text="Milk",variable=var4,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkMilk).grid(row=3,sticky='w')
        self.txtMilk=Entry(f3,font=('arial',12,'bold'),textvariable=Milk,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtMilk.grid(row=3,column=1)

        self.ColdDrink=Checkbutton(f3, text="ColdDrink",variable=var5,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkColdDrink).grid(row=4,sticky='w')
        self.txtColdDrink=Entry(f3,font=('arial',12,'bold'),textvariable=ColdDrink,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtColdDrink.grid(row=4,column=1)

        self.Omlette=Checkbutton(f3, text="Omlette",variable=var6,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkOmlette).grid(row=5,sticky='w')
        self.txtOmlette=Entry(f3,font=('arial',12,'bold'),textvariable=Omlette,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtOmlette.grid(row=5,column=1)

        self.BreadButter=Checkbutton(f3, text="BreadButter",variable=var7,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkBreadButter).grid(row=6,sticky='w')
        self.txtBreadButter=Entry(f3,font=('arial',12,'bold'),textvariable=BreadButter,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtBreadButter.grid(row=6,column=1)

        self.Salad=Checkbutton(f3, text="Salad",variable=var8,onvalue=1,offvalue=0,
                                font=('arial',12,'bold'),bg="#F5D020",command=chkSalad).grid(row=7,sticky='w')
        self.txtSalad=Entry(f3,font=('arial',12,'bold'),textvariable=Salad,bd=8,
                                width=20,justify='left',state='disabled')
        self.txtSalad.grid(row=7,column=1)

        self.lblspace=Label(f3,text="Tax and Total Sum",font=('arial',18,'bold'),pady=1,bd=9,bg="#8703D0",
                            fg="Cornsilk",width=26,justify='center').grid(row=8,column=0,columnspan=4)

            #############################---Bill Value Attributes---#######################

        self.lblPaidTax=Label(f3,font=('arial',12,'bold'),text="Paid Tax",bd=7,bg="#F5D020",fg='black')
        self.lblPaidTax.grid(row=10,column=0, sticky='W')
        self.txtPaidTax=Entry(f3,font=('arial',12,'bold'),textvariable=PaidTax,bd=7,bg='white',width=20,justify='left')
        self.txtPaidTax.grid(row=10,column=1)

        self.lblSubTotal=Label(f3,font=('arial',12,'bold'),text="Sub Total",bd=7,bg="#F5D020",fg='black')
        self.lblSubTotal.grid(row=11,column=0, sticky='W')
        self.txtSubTotal=Entry(f3,font=('arial',12,'bold'),textvariable=SubTotal,bd=7,bg='white',width=20,justify='left')
        self.txtSubTotal.grid(row=11,column=1)

        self.lblTotalCost=Label(f3,font=('arial',12,'bold'),text="Total Cost",bd=7,bg="#F5D020",fg='black')
        self.lblTotalCost.grid(row=12,column=0, sticky='W')
        self.txtTotalCost=Entry(f3,font=('arial',12,'bold'),textvariable=TotalCost,bd=7,bg='white',width=20,justify='left')
        self.txtTotalCost.grid(row=12,column=1)


                ####################################################

        self.lblCus_Ref=Label(f2,font=('arial',12,'bold'),text="Customer Ref:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblCus_Ref.grid(row=0,column=0, sticky='W')
        self.txtCus_Ref=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=CustomerRef)
        self.txtCus_Ref.grid(row=0,column=1,pady=3,padx=20)

        self.lblFirstname=Label(f2,font=('arial',12,'bold'),text="FirstName:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblFirstname.grid(row=1,column=0, sticky='W')
        self.txtFirstname=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1,pady=3,padx=20)

        self.lblSurname=Label(f2,font=('arial',12,'bold'),text="Surname:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblSurname.grid(row=2,column=0, sticky='W')
        self.txtSurname=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Surname)
        self.txtSurname.grid(row=2,column=1,pady=3,padx=20)

        self.lblAddress=Label(f2,font=('arial',12,'bold'),text="Address",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblAddress.grid(row=3,column=0, sticky='W')
        self.txtAddress=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Address)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        self.lblPostCode=Label(f2,font=('arial',12,'bold'),text="PostCode:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblPostCode.grid(row=4,column=0, sticky='W')
        self.txtPostCode=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=PostCode)
        self.txtPostCode.grid(row=4,column=1,pady=3,padx=20)

        self.lblMobile=Label(f2,font=('arial',12,'bold'),text="Mobile:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblMobile.grid(row=5,column=0, sticky='W')
        self.txtMobile=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Mobile)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail=Label(f2,font=('arial',12,'bold'),text="Email:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblEmail.grid(row=6,column=0, sticky='W')
        self.txtEmail=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Email)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblN=Label(f2,font=('arial',12,'bold'),text="Nationality:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblN.grid(row=7,column=0, sticky='W')
        self.cboN=ttk.Combobox(f2,textvariable=Nationality,state='readonly',font=('arial',12,'bold'),width=19)
        self.cboN['value']=('','India','USA','UK','Germany','France','China')
        self.cboN.current(0)
        self.cboN.grid(row=7,column=1,pady=3,padx=20)

        self.lblDOB=Label(f2,font=('arial',12,'bold'),text="DOB:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblDOB.grid(row=8,column=0, sticky='W')
        self.txtDOB=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=DOB)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20)

        self.lblIDType=Label(f2,font=('arial',12,'bold'),text="IDType:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblIDType.grid(row=9,column=0, sticky='W')
        self.cboIDType=ttk.Combobox(f2,textvariable=IDType,state='readonly',font=('arial',12,'bold'),width=19)
        self.cboIDType['value']=('','Driving License','PAN Card','AADHAR Card','Voter Card')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)


        self.lblGender=Label(f2,font=('arial',12,'bold'),text="Gender:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblGender.grid(row=10,column=0, sticky='W')
        self.cboGender=ttk.Combobox(f2,textvariable=Gender,state='readonly',font=('arial',12,'bold'),width=19)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)

        self.lblCheck_In_Date=Label(f2,font=('arial',12,'bold'),text="Check In Date:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblCheck_In_Date.grid(row=11,column=0, sticky='W')
        self.txtCheck_In_Date=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Date1)
        self.txtCheck_In_Date.grid(row=11,column=1,pady=3,padx=20)

        self.lblCheck_Out_Date=Label(f2,font=('arial',12,'bold'),text="Check Out Date:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblCheck_Out_Date.grid(row=12,column=0, sticky='W')
        self.txtCheck_Out_Date=Entry(f2,font=('arial',12,'bold'),width=20,textvariable=Date1)
        self.txtCheck_Out_Date.grid(row=12,column=1,pady=3,padx=20)

        self.lblMeal=Label(f2,font=('arial',12,'bold'),text="Meal:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblMeal.grid(row=13,column=0, sticky='W')
        self.cboMeal=ttk.Combobox(f2,textvariable=Meal,state='readonly',font=('arial',12,'bold'),width=19)
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)


        self.lblRoomType=Label(f2,font=('arial',12,'bold'),text="RoomType:",padx=2,fg="Cornsilk",bg="#8703D0")
        self.lblRoomType.grid(row=14,column=0, sticky='W')
        self.cboRoomType=ttk.Combobox(f2,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=19)
        self.cboRoomType['value']=('','Single','Double')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)




############-------------------TEXT BOX------------#############################

        self.txtReciept = Text(f5, height=19, width=43,bd=10,font=('arial',9,'bold'))
        self.txtReciept.grid(row=0,column=0)

#############---------------------Button--------------------####################

        self.btnTotal = Button(f6, padx=14,pady=7,bd=5,fg="black",font=('arial',16,'bold'),width=5,height=2,
                                bg="#F5D020",text='Total',command=Total).grid(row=0,column=0)
        self.btnReset = Button(f6, padx=14,pady=7,bd=5,fg="black",font=('arial',16,'bold'),width=5,height=2,
                                bg="#F5D020",text='Reset',command=Reset).grid(row=0,column=1)
        self.btnExit = Button(f6, padx=14,pady=7,bd=5,fg="black",font=('arial',16,'bold'),width=5,height=2,
                                bg="#F5D020",text='Exit',command=Exit).grid(row=0,column=2)

################################################################################


if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
