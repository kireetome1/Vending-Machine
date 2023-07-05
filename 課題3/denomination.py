import tkinter as tk
import mysql.connector

# Function to calculate the denomination counts and update the database
def denominate_and_update():
    total_amount = int(amount_entry.get())

    denominations = [1000, 500, 100, 50, 10]
    counts = {}

    # Calculate the count of each denomination
    for denomination in denominations:
        count = total_amount // denomination
        counts[denomination] = count
        total_amount %= denomination

    # Update the denominations in the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="nomi"
    )

    cursor = conn.cursor()

    for denomination, count in counts.items():
        # Assuming you have a table called 'drink' with columns 'En' and 'Quantity'
        query = "UPDATE money SET Quantity =Quantity + %s WHERE En = %s"
        values = (count, denomination)
        cursor.execute(query, values)

    conn.commit()
    conn.close()

    result_label.config(text="Denominations updated successfully!")

# Create the GUI
root = tk.Tk()
root.title("Drink Denomination Updater")

amount_label = tk.Label(root, text="Enter the total amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

update_button = tk.Button(root, text="Update", command=denominate_and_update)
update_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
