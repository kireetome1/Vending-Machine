import mysql.connector
from tkinter import ttk
import tkinter as tk

def View(tree):
    # Establish a connection to the MySQL database
    con1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="nomi"
    )
   
    cur1 = con1.cursor()
   
    # Retrieve data from the table
    cur1.execute("SELECT * FROM money")
    rows = cur1.fetchall()    
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)        
   
    con1.close()

def main():
    root = tk.Tk()
    root.title("Data from the DataBase")

    tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Japanese Yen")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Quantity")
    tree.pack()

    View(tree)

    root.mainloop()
