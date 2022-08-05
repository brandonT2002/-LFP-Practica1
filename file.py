import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


# how to create a table in tkinter using an example
# try and run it for better understanding
from tkinter import *
# creating a class for creating table in tkinter window
class Table:
    def __init__(self,root_2):
        global results
        for i in range(l):
            for j in range(5): # here we use dynamic variable so that you can edit and access the table elements if needed
                exec(f"self.e{i}_{j} = Entry(root_2,width=20,fg='blue',font=('Arial',16,'bold'))")
                exec(f"self.e{i}_{j}.grid(row={i}+2,column={j})")
                exec("self.e"+str(i)+"_"+str(j)+".insert(END, results["+str(i)+"]["+str(j)+"])")
# the data to be placed in table
results = [['1001','SID','CS','100000','18'],['1002','KRISH','BioTech','100000','18'],['1003','GEM','CS','100000','18']]                   
l = len(results)
# main window where the table will be
root_2 = Tk()
root_2.title('Details')
text = Label(root_2,text = "EMPLOYEE DETAILS", font=('Atial',18,'bold')).grid(row=0,column=2)
text = Label(root_2,text = "ID", font=('Atial',16,'bold')).grid(row=1,column=0,sticky=W)
text = Label(root_2,text = "Name", font=('Atial',16,'bold')).grid(row=1,column=1,sticky=W)
text = Label(root_2,text = "Department", font=('Atial',16,'bold')).grid(row=1,column=2,sticky=W)
text = Label(root_2,text = "Salary", font=('Atial',16,'bold')).grid(row=1,column=3,sticky=W)
text = Label(root_2,text = "Age", font=('Atial',16,'bold')).grid(row=1,column=4,sticky=W)
# this is where the class to create the table is called
t = Table(root_2)
root_2.mainloop()