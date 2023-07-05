# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:21:23 2023

@author: new-kensyu
"""

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Returns the change
def Money_Change(amount):
    win = tk.Toplevel()
    win.title("Return Money")
    win.geometry("350x350")

    label = tk.Label(win, text="Your Return is : ", font=('arial black', 15, 'bold'))
    label.place(x=0, y=0)

    label1 = tk.Label(win, text=str(amount), font=('arial black', 15, 'bold'))
    label1.place(x=190, y=0)

# After buying a product, to continue or not
class Continue:
    @staticmethod
    def nextproduct():
        win = tk.Tk()
        win.title("Insufficient Balance")
        win.geometry("350x350")

        label4 = tk.Label(win, text="Do you want to continue buying?", font=('arial black', 15, 'bold'))
        label4.place(x=0, y=0)

        button = tk.Button(win, text="YES", command=win.destroy, font=('arial black', 10, 'bold'), bg='blue',
                           fg="#fff", activebackground="maroon", activeforeground="black")
        button.place(x=100, y=90)

        button = tk.Button(win, text="NO", command=lambda: Money_Change(0), font=('arial black', 10, 'bold'), bg='red',
                           fg="#fff", activebackground="maroon", activeforeground="black")
        button.place(x=170, y=90)

# Money insert window
class InsertMoney:
    def __init__(self, win, total_amount, update_balance):
        self.win = win
        self.total_amount = total_amount
        self.update_balance = update_balance

        self.insert_money_win = tk.Toplevel(self.win)
        self.insert_money_win.title("Insert Money")
        self.insert_money_win.geometry("300x150")

        label = tk.Label(self.insert_money_win, text="Amount to Insert:", font=('arial black', 12, 'bold'))
        label.pack()

        self.amount_entry = tk.Entry(self.insert_money_win, font=('arial black', 12))
        self.amount_entry.pack(pady=10)

        button = tk.Button(self.insert_money_win, text="Insert", command=self.insert_amount, bg='pink',
                           font=('arial black', 10, 'bold'))
        button.pack()

    def insert_amount(self):
        amount = int(self.amount_entry.get())

        # Check if the entered amount is one of the allowed values
        if amount in [10, 50, 100, 500, 1000]:
            self.total_amount += amount
            self.update_balance(self.total_amount)
            self.insert_money_win.destroy()
        else:
            # Display an error message
            messagebox.showerror("Invalid Amount", "Please enter a valid amount (10, 50, 100, 500, or 1000).")

# To check whether the balance is sufficient or not
class balance_Ng:
    @staticmethod
    def balance():
        win = tk.Tk()
        win.title("Insufficient Balance")
        win.geometry("300x300")

        label4 = tk.Label(win, text="Insufficient Balance", font=('arial black', 15, 'bold'))
        label4.place(x=30, y=60)

        button = tk.Button(win, text="Exit", command=win.destroy, font=('arial black', 10, 'bold'), bg='red',
                           fg="#fff", activebackground="maroon", activeforeground="black")
        button.place(x=120, y=90)

# Main class that handles every other class
class MainApp:
    def __init__(self):
        self.total_amount = 0

        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="nomi"
        )

        self.win = tk.Tk()
        self.win.title('Syouhin Mode')
        self.win.geometry('600x600')

        label = tk.Label(self.win, text="Please select the products you want to buy", font=('arial black', 15, 'bold'))
        label.grid(column=0, row=0)

        label1 = tk.Label(self.win, text="Balance:", font=('arial black', 15, 'bold'))
        label1.place(x=360, y=60)

        self.label2 = tk.Label(self.win, text="0", font=('arial black', 15, 'bold'))
        self.label2.place(x=480, y=60)

        label1 = tk.Label(self.win, text="270円", font=('arial black', 15, 'bold'))
        label1.place(x=160, y=60)

        label = tk.Label(self.win, text="250円", font=('arial black', 15, 'bold'))
        label.place(x=100, y=100)

        label = tk.Label(self.win, text="150円", font=('arial black', 15, 'bold'))
        label.place(x=100, y=145)

        label = tk.Label(self.win, text="130円", font=('arial black', 15, 'bold'))
        label.place(x=100, y=190)

        label = tk.Label(self.win, text="170円", font=('arial black', 15, 'bold'))
        label.place(x=100, y=230)

        button = tk.Button(self.win, text="Mango Lassi", command=lambda: self.buy_drink("Mango Lassi", 270),
                           font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                           activeforeground="black")
        button.place(x=30, y=60)

        button1 = tk.Button(self.win, text="Lassi", command=lambda: self.buy_drink("Lassi", 250),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button1.place(x=30, y=100)

        button2 = tk.Button(self.win, text="Coke", command=lambda: self.buy_drink("Coke", 150),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button2.place(x=30, y=145)

        button3 = tk.Button(self.win, text="Fanta", command=lambda: self.buy_drink("Fanta", 130),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button3.place(x=30, y=190)

        button4 = tk.Button(self.win, text="Sprite", command=lambda: self.buy_drink("Sprite", 170),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button4.place(x=30, y=230)

        self.win.mainloop()

    def update_balance(self, amount):
        self.total_amount = amount
        self.label2.config(text=str(self.total_amount))

    def buy_drink(self, drink_name, price):
        if self.total_amount >= price:
            self.total_amount -= price
            self.label2.config(text=str(self.total_amount))
            self.update_database(drink_name, price)
            Continue.nextproduct()
        else:
            balance_Ng.balance()

    def update_database(self, drink_name, price):
        cursor = self.db.cursor()

        # Update the balance in the database
        update_query = "UPDATE users SET balance = balance - %s"
        cursor.execute(update_query, (price,))

        # Insert the purchase details into the purchases table
        insert_query = "INSERT INTO purchases (drink_name, price) VALUES (%s, %s)"
        cursor.execute(insert_query, (drink_name, price))

        self.db.commit()


if __name__ == '__main__':
    app = MainApp()
