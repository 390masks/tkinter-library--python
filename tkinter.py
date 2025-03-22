from tkinter import *
window=Tk()
window.title("Form")
window.geometry("900x900")
window.configure(bg="light blue")

lb=Label(window,text="Besent Technologies \n Enqurey Form",font=16,fg="red")
lb.pack()

frame1=Frame(window,bg="light blue")
frame1.pack(pady=20)

lb1= Label(frame1,text="Date:",bg="light blue",font=14)
lb1.grid(row=0,column=0,sticky="w")

t1=Entry(frame1,width=80)
t1.grid(row=0,column=1,ipady=8)

lb2=Label(frame1,text="Name:",font=14,bg="light blue")
lb2.grid(row=1,column=0,sticky="w")

t2=Entry(frame1,width=80)
t2.grid(row=1,column=1,ipady=8)

lb3=Label(frame1,text="Mobile No:",font=14,bg="light blue")
lb3.grid(row=2,column=0,sticky="w")

t3=Entry(frame1,width=80)
t3.grid(row=2,column=1,ipady=8)

lb4=Label(frame1,text="Alternate No:",bg="light blue",font=14)
lb4.grid(row=3,column=0,sticky="w")

t4=Entry(frame1,width=80)
t4.grid(row=3,column=1,ipady=8)

lb5=Label(frame1,text="Email Id:",bg="light blue",font=14)
lb5.grid(row=4,column=0,sticky="w")

t5=Entry(frame1,width=80)
t5.grid(row=4,column=1,ipady=8)

lb6=Label(frame1,text="Adress:",bg="light blue",font=14)
lb6.grid(row=5,column=0,sticky="w")

t6=Entry(frame1,width=80)
t6.grid(row=5,column=1,ipady=8)

lb7=Label(frame1,text="Coruses Intersted:",bg="light blue",font=14)
lb7.grid(row=6,column=0,sticky="w")

t7=Entry(frame1,width=80)
t7.grid(row=6,column=1,ipady=8)

lb8=Label(frame1,text="Batch Prefered:",bg="light blue",font=14)
lb8.grid(row=7,column=0,sticky="w")

t8=Entry(frame1,width=80)
t8.grid(row=7,column=1,ipady=8)

lb9=Label(frame1,text="How to came to Know about us:",bg="light blue",font=14)
lb9.grid(row=8,column=0,sticky="w")

t9=Entry(frame1,width=80)
t9.grid(row=8,column=1,ipady=8)

lb10=Label(frame1,text="Are you Expireanced or fresher:",bg="light blue",font=14)
lb10.grid(row=9,column=0,sticky="w")

t10=Entry(frame1,width=80)
t10.grid(row=9,column=1,ipady=8)

lb11=Label(frame1,text="Contact preson from Besent Technologies:",bg="light blue",font=14)
lb11.grid(row=10,column=0,sticky="w")

t11=Entry(frame1,width=80)
t11.grid(row=10,column=1,ipady=8)

lb12=Label(frame1,text="Conuselor:",bg="light blue",font=14)
lb12.grid(row=11,column=0,sticky="w")

t12=Entry(frame1,width=80)
t12.grid(row=11,column=1,ipady=8)

lb13=Label(frame1,text="Fees:",bg="light blue",font=14)
lb13.grid(row=12,column=0,sticky="w")

t13=Entry(frame1,width=80)
t13.grid(row=12,column=1,ipady=8)

lb14=Label(frame1,text="Comment:",bg="light blue",font=14)
lb14.grid(row=13,column=0,sticky="w")

t14=Entry(frame1,width=80)
t14.grid(row=13,column=1,ipady=8)

var1=IntVar()
check_frame = Frame(frame1, bg="light blue")
check_frame.grid(row=15, column=1, sticky="w")


check1 = Checkbutton(check_frame, text="Enquiry", variable=var1)
check1.pack(side="left", padx=(0, 10))

var2=IntVar()
check2 = Checkbutton(check_frame, text="Registration", variable=var2)
check2.pack(side="left")


button_frame=Frame(frame1,bg="light blue")
button_frame.grid(row=16,column=1,sticky="w")

but1=Button(button_frame,text="Submit",bg="green")
but1.pack(side="left",padx=(0,10),ipadx=10)

but2=Button(button_frame,text="Quite",bg="red")
but2.pack(side="left",padx=(0,10),ipadx=5)

window.mainloop()
