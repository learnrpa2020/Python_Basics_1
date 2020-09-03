from tkinter import *
from tkinter import ttk

root=Tk()
namelbl=ttk.Label(root,text="Name").place(x=10,y=10)
nameentry=ttk.Entry(root,width=30).place(x=100,y=10)
passlbl=ttk.Label(root,text="Password").place(x=10,y=50)
password=ttk.Entry(root,width=30,show="*").place(x=100,y=50)
Courselbl=ttk.Label(root,text="Known Language").place(x=0,y=100)
java=ttk.Checkbutton(root,text="Java").place(x=120,y=100)
python=ttk.Checkbutton(root,text="Python").place(x=170,y=100)
sql=ttk.Checkbutton(root,text="SQL").place(x=240,y=100)
Gender=ttk.Label(root,text="Gender").place(x=10,y=150)
Male=ttk.Radiobutton(root,text="Male",value='Male').place(x=100,y=150)
Female=ttk.Radiobutton(root,text="Female",value='Female').place(x=150,y=150)
doblbl=ttk.Label(root,text="DOB").place(x=10,y=200)
month=StringVar()
combobox=ttk.Combobox(root,text=month,values=('Jan','Feb','Mar','Apr','May',
                                              'Jun','Jul','Aug','Sep','Oct','Nov','Dec')).place(x=50,y=200)
year=StringVar()
spinbox=Spinbox(root,text=year,from_=1980,to=2020).place(x=200,y=200)
submit=ttk.Button(root,text="Submit").place(x=200,y=250)