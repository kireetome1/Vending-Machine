import tkinter as tk
import mysql.connector

#gives the message that the product is added
class productadd:
        def add():
            win=tk.Tk()
            win.title("Product Add")
            win.geometry("390x220")
            
            label4 = tk.Label(win, text="Product Added Successfully", font=('arial black', 15, 'bold'))
            label4.place(x=0, y=60)
            
            button = tk.Button(win, text="Exit", command=win.destroy,font=('arial black', 10, 'bold'), bg='red', fg="#fff", activebackground="maroon",activeforeground="black")
            button.place(x=160, y=100)

#creates a window having buttons to add the needed products
class MainApp:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Product ADD')
        self.win.geometry('620x400')

        label = tk.Label(self.win, text="Please select the products you want to ADD", font=('arial black', 15, 'bold'))
        label.grid(column=0, row=0)

        button = tk.Button(self.win, text="Mango Lassi", command=lambda: self.add_drink("Mango Lassi", 250),
                           font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                           activeforeground="black")
        button.place(x=30, y=60)

        button1 = tk.Button(self.win, text="Lassi", command=lambda: self.add_drink("Lassi", 150),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button1.place(x=30, y=100)

        button2 = tk.Button(self.win, text="Coke", command=lambda: self.add_drink("Coke", 130),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button2.place(x=30, y=145)

        button3 = tk.Button(self.win, text="Fanta", command=lambda: self.add_drink("Fanta", 170),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button3.place(x=30, y=190)

        button4 = tk.Button(self.win, text="Sprite", command=lambda: self.add_drink("Sprite", 270),
                            font=('arial black', 10, 'bold'), bg='blue', fg="#fff", activebackground="maroon",
                            activeforeground="black")
        button4.place(x=30, y=230)
        
        button = tk.Button(self.win, text="Exit", command=self.win.destroy,
                           font=('arial black', 10, 'bold'), bg='red', fg="#fff", activebackground="maroon",
                           activeforeground="black")
        button.place(x=270, y=280)

        self.win.mainloop()

#adds/updates the drink table of the database
    def add_drink(self, drink_name, price):
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
            query = "UPDATE drink SET Quantity = Quantity + 1 WHERE name = %s"

            # Execute the SQL query
            cursor.execute(query, (drink_name,))

            # Commit the changes to the database
            conn.commit()

            # Show a success message or perform any other necessary actions
            print("Drink added successfully: ", drink_name)
            productadd.add()
        except mysql.connector.Error as e:
            print("Database Error:", e)
        finally:
            # Close the cursor and database connection
            cursor.close()
            conn.close()


# Create an instance of the MainApp class
#main_app = MainApp()
