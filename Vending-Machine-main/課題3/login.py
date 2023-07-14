from tkinter import Tk, Label, Button, messagebox, Entry, Checkbutton, IntVar
import drink
import kanri

##### Login Page #####

class Login_Page:
    def __init__(self):
        self.login = Tk()
        self.login.protocol("WM_DELETE_WINDOW", self.event_x)
        self.login.title("Vending Machine")
        self.login.geometry("450x230+450+170")

        # Creating description labels
        self.username_label = Label(self.login, text="Username:")
        self.username_label.place(relx=0.230, rely=0.298, height=20, width=70)

        self.password_label = Label(self.login, text="Password:")
        self.password_label.place(relx=0.230, rely=0.468, height=20, width=65)

        # Creating Buttons
        self.login_button = Button(self.login, text="Login", command=self.login_user)
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)

        self.exit_button = Button(self.login, text="Exit", command=self.exit_login)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)

        # Creating entry boxes
        self.username_box = Entry(self.login)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = Entry(self.login)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        # Creating checkbox
        #self.show_password_var = IntVar()
        #self.show_password_checkbox = Checkbutton(self.login, text="Show", variable=self.show_password_var,
        #                                          command=self.toggle_password_visibility)
        #self.show_password_checkbox.place(relx=0.285, rely=0.650, relheight=0.100, relwidth=0.125)

    def event_x(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.login.destroy()

    #def toggle_password_visibility(self):
    #    if self.show_password_var.get() == 1:
    #        self.password_box.configure(show="")
    #    else:
    #        self.password_box.configure(show="*")

    def login_user(self):
        name = self.username_box.get()
        password = self.password_box.get()

        if name == "bishnu" and password == "11111":
            messagebox.showinfo("Login Successful", "Login successful!")
            self.login.destroy()
            kanri.main()
        else:
            messagebox.showwarning("Login Failed", "Access Denied. Username or Password incorrect!")

    def exit_login(self):
        if messagebox.askyesno("Exit Login Page", "Do you really want to exit?"):
            self.login.destroy()


if __name__ == "__main__":
    login_page = Login_Page()
    login_page.login.mainloop()
