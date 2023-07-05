#import login
import tkinter as tk
import drink
import money
import productplus

#defining the entered button
def open_file():
    drink.main()
    
def paisa():
    money.main()
    
def product_add():
    productplus.MainApp()


#creating windows
def main():
    win = tk.Tk()
    win.title('Vending Machine')
    win.geometry('550x400')
     
    #labeling the title
    label1 = tk.Label(win, text='Please select an option',font=('arial black', 25), bg="black", fg="#fff")
    label1.grid(column=3,row=2)


    #creating a gui button
    button=tk.Button(win,text='Product verification',command=open_file,font=('arial black', 20,'bold'),bg='blue', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
    button.grid(column=3,row=3,rowspan=1,columnspan=3)

    button1=tk.Button(win,text='Money Verification',command=paisa,font=('arial black', 20,'bold'),bg='blue', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
    button1.grid(column=3,row=4)
    #button1.bind("<Button>",lambda e: loginp1())

    button2=tk.Button(win,text='Insert products',command=product_add,font=('arial black', 20,'bold'),bg='blue', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
    button2.grid(column=3,row=5)
    
    button3=tk.Button(win,text='Exit',command=win.destroy,font=('arial black', 20,'bold'),bg='red', fg="#fff", activebackground="maroon", activeforeground="black")#insert command later on
    button3.place(x=220,y=310)

    win.mainloop()

