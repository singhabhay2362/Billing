from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime



class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #Variables
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()


        #Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobile"]

        #SubCatClothing
        self.SubCatClothing=['Jeans','T-Shirts','Shirts']
        self.Jeans=['Roadster','H&M','Levis','Killer','Mast Harbour','Highlander']
        self.price_roadster=2000
        self.price_hm=5000
        self.price_lev=6000
        self.price_killer=4500
        self.price_mastharbour=1600
        self.price_highlander=2999

        self.T_Shirts=['Jockey','Jack & Jhones','Flying Machine','HRX','Prowl','Under Armour']
        self.price_jockey=599
        self.price_jackjones=399
        self.price_flymachine=699
        self.price_hrx=999
        self.price_prowl=1299
        self.price_uarmour=4999

        self.Shirts=['Peter England','Mufti','Monte Carlo','Denis Lingo','Louis Phillipene']
        self.price_peterengland=3999
        self.price_mufti=2999
        self.price_montecarlo=5999
        self.price_denislingo=999
        self.price_louisp=6999

        #SubCatLifeStyle
        self.SubCatLifeStyle=['Soap','Face Wash','Hair Oil','Cream']
        self.Soap=['Pears','Lux','Wild Stone','Lifeboy','Liril']
        self.price_pears=20
        self.price_lux=20
        self.price_wildstone=20
        self.price_lifeboy=10
        self.price_liril=20

        self.Face_Wash=['Garnier','Nevia','Fair & Handsome','Beardo']
        self.price_garnier=95
        self.price_nevia=65
        self.price_fairhandsome=60
        self.price_beardo=105

        self.Hair_Oil=['Parachute','Jasmine','Bajaj']
        self.price_parachute=35
        self.price_jasmine=40
        self.price_bajaj=55

        self.Cream=['Ponds','Olay','Biotique']
        self.price_ponds=32
        self.price_olay=93
        self.price_biotique=125

        #Mobiles
        self.SubCatMobiles=['RealMe','Samsung','Xiomi']
        self.RealMe=['5 pro','Narzo','C11','6 pro']
        self.price_5pro=11000
        self.price_Narzo=15000
        self.price_C11=9000
        self.price_6pro=16000

        self.Samsung=['Samsung M16','Samsung M21','Samsung J2']
        self.price_sm16=16000
        self.price_sm21=20000
        self.price_smj2=14000

        self.Xiomi=['Red11','Red-12','Redmi Pro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        lbl_title=Label(self.root,text="BILLING SOFTWARE ",font=("times new roman",35,"bold"),bg="black",fg="red")
        lbl_title.place(x=0,y=0,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='black',foreground='white')
        lbl.place(x=0,y=0,width=120,height=50)
        time()

        #MAIN_FRAME
        Main_Frame=Frame(self.root,bd=6,relief=GROOVE,bg="black")
        Main_Frame.place(x=0,y=48,width=1530,height=720)

        #CUSTOMER_FRAME
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",10,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',10,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',10,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #PRODUCT_FRAME
        Product_Frame=LabelFrame(Main_Frame,text="Product Details", font=("times new roman", 10, "bold"), bg="white",fg="red")
        Product_Frame.place(x=370, y=5, width=600, height=140)

        #CATEGORY
        self.lblCategory = Label(Product_Frame, font=('arial', 10, 'bold'), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category= ttk.Combobox(Product_Frame,value=self.Category, font=('arial',8, 'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SUB_CATEGORY
        self.lblSubCategory=Label(Product_Frame,font=('arial',8, 'bold'),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',8,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #PRODUCT NAME
        self.lblproduct=Label(Product_Frame,font=('arial',8, 'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',8,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #PRICE
        self.lblPrice = Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',8,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #QTY
        self.lblQty=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2 ,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',8,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #MIDDLE FRAME
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=180,width=980,height=360)

        #image
        img = Image.open("images/pic1.jpg")
        img = img.resize((490,600), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(MiddleFrame,image=self.photoimg)
        lbl_img.place(x = 0, y = 0, width = 490, height = 340)

        #image2
        img_1 = Image.open("images/pic2.jpg")
        img_1 = img_1.resize((490,600), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(MiddleFrame,image=self.photoimg_1)
        lbl_img_1.place(x=490,y=0,width=470,height=340)

        #SEARCH
        Search_Frame=Frame(Main_Frame,bd=2,bg="black")
        Search_Frame.place(x=1020,y=15,width=400,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',10,'bold'),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',8,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',8,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        #RIGHT FRAME
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",10,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=520)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.configure(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #BILL COUNTER LABEL FRAME
        BillCounter_Frame = LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman", 10, "bold"),bg="white",fg="red")
        BillCounter_Frame.place(x=0, y=580,width=1520,height=125)

        self.lblSubTotal= Label(BillCounter_Frame,font=('arial', 10, 'bold'), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0,column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal= ttk.Entry(BillCounter_Frame,font=('arial', 8, 'bold'), width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W, padx=5,pady=2)

        self.lbl_tax = Label(BillCounter_Frame,font=('arial', 10, 'bold'), bg="white", text="Gov. Tax", bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5, pady=2)

        self.Entry_tax= ttk.Entry(BillCounter_Frame,font=('arial',8,'bold'), width=24)
        self.Entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(BillCounter_Frame,font=('arial',10,'bold'),bg="white",text="Total", bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.EntryAmountTotal=ttk.Entry(BillCounter_Frame,font=('arial', 8,'bold'),width=24)
        self.EntryAmountTotal.grid(row=2, column=1,sticky=W,padx=5,pady=2)

        #BUTTON
        Btn_Frame=Frame(BillCounter_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add TO Cart",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill ",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint= Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="blue",width=15,cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.welcome()
        self.l=[]

    #=================function declaration=====================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t\tVisit Us Again")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END, f"\nCustomer E-Mail:{self.c_email.get()}")

        self.textarea.insert(END,"\n=================================================================")
        self.textarea.insert(END, f"\n Products\t\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END, "\n=================================================================\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()} \t\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=================================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=================================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('E:\Billing Software\Bills/'+str(self.bill_no.get())+".text",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved Bill",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("E:\Billing Software\Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1.open(f'E:\Billing Software\Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        z = random.randint(1000, 9999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.sub_total.set("")
        self.tax_input.set('')
        self.total.set("")
        self.l=[0]
        self.welcome()

    def Categories(self,events=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobile":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Jeans":
            self.ComboProduct.config(value=self.Jeans)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirts":
            self.ComboProduct.config(value=self.T_Shirts)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirts":
            self.ComboProduct.config(value=self.Shirts)
            self.ComboProduct.current(0)

        #LifeStyle
        if self.ComboSubCategory.get()=="Soap":
            self.ComboProduct.config(value=self.Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Wash":
            self.ComboProduct.config(value=self.Face_Wash)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Cream":
            self.ComboProduct.config(value=self.Cream)
            self.ComboProduct.current(0)

        #Mobile 'RealMe','Samsung','Xiomi'
        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiomi":
            self.ComboProduct.config(value=self.Xiomi)
            self.ComboProduct.current(0)

    def price(self,event=""):
        #Jeans
        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="H&M":
            self.ComboPrice.config(value=self.price_hm)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_lev)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Killer":
            self.ComboPrice.config(value=self.price_killer)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mast Harbour":
            self.ComboPrice.config(value=self.price_mastharbour)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Highlander":
            self.ComboPrice.config(value=self.price_highlander)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T_Shirts
        if self.ComboProduct.get()=="Jockey":
            self.ComboPrice.config(value=self.price_jockey)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack & Jhones":
            self.ComboPrice.config(value=self.price_jackjones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Flying Machine":
            self.ComboPrice.config(value=self.price_flymachine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="HRX":
            self.ComboPrice.config(value=self.price_hrx)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Prowl":
            self.ComboPrice.config(value=self.price_prowl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Under Armour":
            self.ComboPrice.config(value=self.price_uarmour)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirts
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_peterengland)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Monte Carlo":
            self.ComboPrice.config(value=self.price_montecarlo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Denis Lingo":
            self.ComboPrice.config(value=self.price_denislingo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipene":
            self.ComboPrice.config(value=self.price_louisp)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Moblie
        if self.ComboProduct.get() == "5 pro":
            self.ComboPrice.config(value=self.price_5pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Narzo":
            self.ComboPrice.config(value=self.price_Narzo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "C11":
            self.ComboPrice.config(value=self.price_C11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "6 pro":
            self.ComboPrice.config(value=self.price_6pro)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get() == "Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung J2":
            self.ComboPrice.config(value=self.price_smj2)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get() == "Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Red-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Redmi Pro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #LifeStyle
        if self.ComboProduct.get() == "Pears":
            self.ComboPrice.config(value=self.price_pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Wild Stone":
            self.ComboPrice.config(value=self.price_wildstone)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lifeboy":
            self.ComboPrice.config(value=self.price_lifeboy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Liril":
            self.ComboPrice.config(value=self.price_liril)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Garnier','Nevia','Fair & Handsome','Beardo'
        if self.ComboProduct.get() == "Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Nevia":
            self.ComboPrice.config(value=self.price_nevia)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Fair & Handsome":
            self.ComboPrice.config(value=self.price_fairhandsome)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Beardo":
            self.ComboPrice.config(value=self.price_beardo)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(value=self.price_parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jasmine":
            self.ComboPrice.config(value=self.price_jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #'Ponds','Olay','Biotique'
        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Biotique":
            self.ComboPrice.config(value=self.price_biotique)
            self.ComboPrice.current(0)
            self.qty.set(1)


if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
