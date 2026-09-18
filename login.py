import tkinter as tk
from tkinter import messagebox
import database


class LoginWindow:

    def __init__(self):

        print("Creating window")

        self.root = tk.Tk()
        self.root.title("AI Resume Analyzer")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        # Bring window to front
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(
            100,
            lambda: self.root.attributes("-topmost", False)
        )


        # Title
        tk.Label(
            self.root,
            text="AI Resume Analyzer",
            font=("Arial", 18, "bold")
        ).pack(pady=20)


        # Username
        tk.Label(
            self.root,
            text="Username"
        ).pack()

        self.username = tk.Entry(
            self.root,
            width=30
        )
        self.username.pack(pady=5)


        # Password
        tk.Label(
            self.root,
            text="Password"
        ).pack()

        self.password = tk.Entry(
            self.root,
            width=30,
            show="*"
        )
        self.password.pack(pady=5)


        # Login Button
        tk.Button(
            self.root,
            text="Login",
            width=20,
            command=self.login
        ).pack(pady=10)


        # Register Button
        tk.Button(
            self.root,
            text="Register",
            width=20,
            command=self.register
        ).pack()


        print("Starting mainloop")

        self.root.mainloop()



    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror(
                "Error",
                "Enter Username and Password"
            )
            return


        if database.login(user, pwd):

            messagebox.showinfo(
                "Success",
                "Login Successful!"
            )

            self.root.destroy()

            import dashboard
            dashboard.Dashboard()

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )



    def register(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror(
                "Error",
                "Enter Username and Password"
            )
            return


        if database.register(user, pwd):

            messagebox.showinfo(
                "Success",
                "Registration Successful"
            )

        else:

            messagebox.showerror(
                "Error",
                "Username Already Exists"
            )



if __name__ == "__main__":

    print("Opening LoginWindow")

    LoginWindow()