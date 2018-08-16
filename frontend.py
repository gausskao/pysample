from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[0])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[2])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[3])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[4])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[5])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[6])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[7])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[8])
    e10.delete(0,END)
    e10.insert(END,selected_tuple[9])
    e11.delete(0,END)
    e11.insert(END,selected_tuple[10])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(int(id_text.get()),status_text.get(),country_text.get(),city_text.get(),startdate_text.get(),enddate_text.get(),\
    team_text.get(),name_text.get(),maintask_text.get(),address_text.get(),telno_text.get())
    list1.delete(0,END)
    #list1.insert(END,(int(id_text.get()),status_text.get(),country_text.get(),city_text.get(),startdate_text.get(),enddate_text.get(),\
    #team_text.get(),name_text.get(),maintask_text.get(),address_text.get(),telno_text.get()))
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command();

def update_command():
    backend.update(int(id_text.get()),status_text.get(),country_text.get(),city_text.get(),startdate_text.get(),enddate_text.get(),\
    team_text.get(),name_text.get(),maintask_text.get(),address_text.get(),telno_text.get())
    view_command()

window=Tk()

window.wm_title("QMC AIT onsite schedule")

l1=Label(window,text="ID")
l1.grid(row=0,column=0)

l2=Label(window,text="Status")
l2.grid(row=0,column=1)

l3=Label(window,text="Country")
l3.grid(row=0,column=2)

l4=Label(window,text="City")
l4.grid(row=0,column=3)

l5=Label(window,text="Start Date")
l5.grid(row=0,column=4)

l6=Label(window,text="End Date")
l6.grid(row=0,column=5)

l7=Label(window,text="Team")
l7.grid(row=0,column=6)

l8=Label(window,text="Name")
l8.grid(row=0,column=7)

l9=Label(window,text="Main Task")
l9.grid(row=0,column=8)

l10=Label(window,text="Hotel name and address")
l10.grid(row=0,column=9)

l11=Label(window,text="Phone No")
l11.grid(row=0,column=10)

id_text=StringVar()
e1=Entry(window,textvariable=id_text)
e1.grid(row=1,column=0)

status_text=StringVar()
e2=Entry(window,textvariable=status_text)
e2.grid(row=1,column=1)

country_text=StringVar()
e3=Entry(window,textvariable=country_text)
e3.grid(row=1,column=2)

city_text=StringVar()
e4=Entry(window,textvariable=city_text)
e4.grid(row=1,column=3)

startdate_text=StringVar()
e5=Entry(window,textvariable=startdate_text)
e5.grid(row=1,column=4)

enddate_text=StringVar()
e6=Entry(window,textvariable=enddate_text)
e6.grid(row=1,column=5)

team_text=StringVar()
e7=Entry(window,textvariable=team_text)
e7.grid(row=1,column=6)

name_text=StringVar()
e8=Entry(window,textvariable=name_text)
e8.grid(row=1,column=7)

maintask_text=StringVar()
e9=Entry(window,textvariable=maintask_text)
e9.grid(row=1,column=8)

address_text=StringVar()
e10=Entry(window,textvariable=address_text)
e10.grid(row=1,column=9)

telno_text=StringVar()
e11=Entry(window,textvariable=telno_text)
e11.grid(row=1,column=10)

list1=Listbox(window, height=12,width=210)
list1.grid(row=2,column=0,rowspan=12,columnspan=10)

sb1=Scrollbar(window)
sb1.grid(row=2,column=10,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=11)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=11)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=11)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=11)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=11)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=11)

view_command()

window.mainloop()