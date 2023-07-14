import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Returns the change
def Money_Change(amount):
    win = tk.Toplevel()
    win.title("Return Money")
    win.geometry("300x150")

    label = tk.Label(win, text="Your Return is : ", font=('arial black', 15, 'bold'))
    label.place(x=0, y=0)

    label1 = tk.Label(win, text=str(amount), font=('arial black', 15, 'bold'))
    label1.place(x=190, y=0)


# After buying a product, to continue or not
class ContinuePurchase:
    @staticmethod
    def nextproduct():
        win = tk.Tk()
        win.title("Drink Bought")
        win.geometry("310x150")

        label4 = tk.Label(win, text="Drink Bought Successfully!!", font=('arial black', 15, 'bold'))
        label4.place(x=0, y=0)

        button = tk.Button(win, text="EXIT", command=win.destroy, font=('arial black', 10, 'bold'), bg='red',
                           fg="white", activebackground="red", activeforeground="black")
        button.place(x=120, y=50)


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

        button = tk.Button(self.insert_money_win, text="Insert", command=self.insert_amount, bg='silver',
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

        label4 = tk.Label(win, text="Insufficient Balance", font=('arial black', 15, 'bold'))
        label4.place(x=30, y=60)

        button = tk.Button(win, text="Exit", command=win.destroy, font=('arial black', 10, 'bold'), bg='red',
                           fg="#fff", activebackground="red", activeforeground="black")
        button.place(x=120, y=90)


# Main class that handles every other class
class MainApp:
    def __init__(self):
        self.total_amount = 0

        self.win = tk.Tk()
        self.win.title('Syouhin Mode')
        self.win.geometry('600x400')

        label = tk.Label(self.win, text="Please select the products you want to buy",
                         font=('arial black', 15, 'bold'))
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

        insert = tk.Button(self.win, text="Insert Money", command=self.insert_money, font=('arial black', 10, 'bold'),
                           bg='silver', fg="black", activebackground="maroon", activeforeground="black")
        insert.place(x=400, y=300)

        return_money = tk.Button(self.win, text="Return Money", command=self.return_money,
                                 font=('arial black', 10, 'bold'),
                                 bg='maroon', fg="#fff", activebackground="maroon", activeforeground="black")
        return_money.place(x=400, y=350)

        EXIT = tk.Button(self.win, text="Exit", command=lambda: [self.close_current_window(), self.open_new_window()],
                         font=('arial black', 10, 'bold'),
                         bg='red', fg="#fff", activebackground="maroon", activeforeground="black")
        EXIT.place(x=120, y=300, height=70, width=70)

        self.win.mainloop()

    def close_current_window(self):
        self.win.destroy()

    def open_new_window(self):
        Money_Change(self.total_amount)
        self.total_amount = 0
        self.label2.config(text="0")

    def insert_money(self):
        InsertMoney(self.win, self.total_amount, self.update_balance)

    def update_balance(self, amount):
        self.total_amount = amount
        self.label2.config(text=str(self.total_amount))

    def return_money(self):
        Money_Change(self.total_amount)
        self.total_amount = 0
        self.label2.config(text="0")

    def buy_drink(self, drink_name, price):
        if self.total_amount >= price:
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

                # Update the database with the purchased drink
                query = "UPDATE drink SET Quantity = Quantity - 1 WHERE name = %s"

                # Execute the SQL query
                cursor.execute(query, (drink_name,))

                # Commit the changes to the database
                conn.commit()

                # Subtract the price from the total amount
                self.total_amount -= price

                # Update the balance label
                self.label2.config(text=str(self.total_amount))

                # Show a success message or perform any other necessary actions
                print("Drink purchased successfully: ", drink_name)

                denominations = [1000, 500, 100, 50, 10]
                counts = {}

                # Calculate the count of each denomination
                for denomination in denominations:
                    count = self.total_amount // denomination
                    counts[denomination] = count
                    self.total_amount %= denomination

                # Update the denominations in the database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="nomi"
                )

                cursor = conn.cursor()

                for denomination, count in counts.items():
                    # Assuming you have a table called 'money' with columns 'En' and 'Quantity'
                    query = "UPDATE money SET Quantity = Quantity + %s WHERE En = %s"
                    values = (count, denomination)
                    cursor.execute(query, values)
#                    result_label.config(text="Denominations updated successfully!")

                # to proceed or not
#                Continue.nextproduct()

            except mysql.connector.Error as e:
                print("Database Error:", e)
            finally:
                # Close the cursor and database connection
                cursor.close()
                conn.close()
        else:
            # Show an error message or perform any other necessary actions
            print("Insufficient balance to purchase the drink.")
            balance_Ng.balance()


