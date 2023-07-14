# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:37:25 2023

@author: new-kensyu
"""
import login
import newsyouhin
import tkinter as tk

#creating windows
win = tk.Tk()
win.title('Vending Machine')
win.geometry('640x500')

def new_login():
    login.Login_Page()
    
def new_syouhin():
    newsyouhin.MainApp()


  
#labeling the title
label = tk.Label(win, text='Vending Machine',font=('arial black', 40,'bold'), bg="green", fg="#fff", activebackground="#f00", activeforeground="red")
label.grid(column=3,row=0)


label1 = tk.Label(win, text='Welcome to the Vending Machine',font=('arial black', 15), bg="silver", fg="black")
label1.grid(column=3,row=1,rowspan=1)

label1 = tk.Label(win, text='Please select an option',font=('arial black', 15), bg="silver", fg="black")
label1.grid(column=3,row=2)


#creating a gui button
button=tk.Button(win,text='Syouhinn Mode',command=new_syouhin,font=('arial black', 20,'bold'),bg='blue', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
button.grid(column=3,row=3,rowspan=1,columnspan=3)

button1=tk.Button(win,text='Kanri Mode',font=('arial black', 20,'bold'),command=new_login,bg='blue', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
button1.grid(column=3,row=4)
#button1.bind("<Button>",lambda e: loginp1())

#root.quit asks for option to quit or not
#where as destroy destroys the window
button2=tk.Button(win,text='Exit',command=win.destroy,font=('arial black', 20,'bold'),bg='red', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
button2.grid(column=3,row=5)

win.mainloop()

