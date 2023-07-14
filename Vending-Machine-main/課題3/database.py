# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:20:51 2023

@author: new-kensyu
"""

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Returns the change
def Money_Change(amount):
    win = tk.Toplevel()
    win.title("Return Money")
    win.geometry("300x150")

    label = tk.Label(win, text="返却お金は : ", font=('arial black', 15, 'bold'))
    label.place(x=0, y=0)

    label1 = tk.Label(win, text=str(amount), font=('arial black', 15, 'bold'))
    label1.place(x=190, y=0)

# After buying a product, to continue or not
class Continue:
    @staticmethod
    def nextproduct():
        win = tk.Tk()
        win.title("Drink Bought")
        win.geometry("310x150")

        label4 = tk.Label(win, text="ドリングを買いました", font=('arial black', 15, 'bold'))
        label4.place(x=0, y=0)

        button = tk.Button(win, text="閉じる", command=win.destroy, font=('arial black', 10, 'bold'), bg='red',
                           fg="white", activebackground="red", activeforeground="black")
        button.place(x=120, y=50)

# Money insert window
class InsertMoney:
    def __init__(self, win, total_amount, update_balance):
        self.win = win
        self.total_amount = total_amount
        self.update_balance = update_balance

        self.insert_money_win = tk.Toplevel(self.win)
        self.insert_money_win.title("投入金額")
        self.insert_money_win.geometry("300x150")

        label = tk.Label(self.insert_money_win, text="お金を入れてください:", font=('arial black', 12, 'bold'))
        label.pack()

        self.amount_entry = tk.Entry(self.insert_money_win, font=('arial black', 12))
        self.amount_entry.pack(pady=10)

        button = tk.Button(self.insert_money_win, text="投入", command=self.insert_amount, bg='silver',
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
        win.geometry("300x200")

        label4 = tk.Label(win, text="お金が足りません", font=('arial black', 15, 'bold'))
        label4.place(x=30, y=60)

        button = tk.Button(win, text="閉じる", command=win.destroy, font=('arial black', 10, 'bold'), bg='red',
                           fg="#fff", activebackground="red", activeforeground="black")
        button.place(x=120, y=90)

# Main class that handles every other class
class MainApp:
    def __init__(self):
        self.total_amount = 0

        self.win = tk.Tk()
        self.win.title('Syouhin Mode')
        self.win.geometry('600x400')

        # Get the money values from the database
        self.money_values = self.get_money_values_from_database()

        # Labels
        self.label = tk.Label(self.win, text='金額:', font=('arial black', 15, 'bold'))
        self.label.place(x=0, y=0)

        self.label2 = tk.Label(self.win, text=str(self.total_amount), font=('arial black', 15, 'bold'))
        self.label2.place(x=200, y=0)

        self.label3 = tk.Label(self.win, text='お金を投入してください:', font=('arial black', 15, 'bold'))
        self.label3.place(x=0, y=50)

        # Buttons
        self.insert_button = tk.Button(self.win, text='投入金額', command=self.insert_money,
                                       font=('arial black', 12))
        self.insert_button.place(x=220, y=100)

        self.buy_button = tk.Button(self.win, text='ドリングを買う', command=self.buy_drink, font=('arial black', 12))
        self.buy_button.place(x=240, y=150)

        self.quit_button = tk.Button(self.win, text='閉じる', command=self.win.quit, font=('arial black', 12))
        self.quit_button.place(x=260, y=200)

        self.win.mainloop()

    def insert_money(self):
        InsertMoney(self.win, self.total_amount, self.update_balance)

    def update_balance(self, amount):
        self.total_amount = amount
        self.label2.config(text=str(self.total_amount))

    def buy_drink(self):
        if self.total_amount >= 100:
            self.total_amount -= 100
            self.update_balance(self.total_amount)
            Continue.nextproduct()
        else:
            balance_Ng.balance()

    def get_money_values_from_database(self):
        try:
            # Establish a database connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="nomi"
            )

            # Create a cursor object
            cursor = conn.cursor()

            # Fetch the money values from the database
            query = "SELECT * FROM money"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Convert rows into a dictionary with value as the key and quantity as the value
            money_values = {row[0]: row[1] for row in rows}

            # Close the cursor and database connection
            cursor.close()
            conn.close()

            return money_values

        except mysql.connector.Error as e:
            print("Database Error:", e)

    def update_money_in_database(self):
        try:
            # Establish a database connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="nomi"
            )

            # Create a cursor object
            cursor = conn.cursor()

            # Fetch the existing money values from the database
            query = "SELECT * FROM money"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Initialize the quantities dictionary
            quantities = {row[0]: row[1] for row in rows}

            # Convert the total amount into denominations of 10, 50, 100, 500, and 1000
            denominations = [1000, 500, 100, 50, 10]
            for denom in denominations:
                quantity = self.total_amount // denom
                if quantities[denom] >= quantity:
                    quantities[denom] -= quantity
                    self.total_amount %= denom
                else:
                    self.total_amount -= quantities[denom] * denom
                    quantities[denom] = 0

            # Update the money values in the database
            for denom, quantity in quantities.items():
                query = f"UPDATE money SET quantity={quantity} WHERE value={denom}"
                cursor.execute(query)

            # Commit the changes and close the cursor and database connection
            conn.commit()
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            print("Database Error:", e)

# Run the application
if __name__ == '__main__':
    MainApp()
