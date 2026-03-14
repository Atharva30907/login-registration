import customtkinter as ctk

# Basic configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Auth System")
        self.geometry("400x500")

        # Container to hold the frames
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, fill="both", padx=20, pady=20)

        self.show_login()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        
        # Title
        label = ctk.CTkLabel(self.container, text="Login", font=("Roboto", 24, "bold"))
        label.pack(pady=30)

        # Inputs
        self.username = ctk.CTkEntry(self.container, placeholder_text="Username", width=250, height=40)
        self.username.pack(pady=12)

        self.password = ctk.CTkEntry(self.container, placeholder_text="Password", show="*", width=250, height=40)
        self.password.pack(pady=12)

        # Buttons
        login_btn = ctk.CTkButton(self.container, text="Login", width=250, height=40, command=self.login_event)
        login_btn.pack(pady=24)

        switch_btn = ctk.CTkButton(self.container, text="Create Account", fg_color="transparent", 
                                   hover_color="#333333", command=self.show_registration)
        switch_btn.pack()

    def show_registration(self):
        self.clear_frame()

        label = ctk.CTkLabel(self.container, text="Register", font=("Roboto", 24, "bold"))
        label.pack(pady=30)

        self.reg_user = ctk.CTkEntry(self.container, placeholder_text="Choose Username", width=250, height=40)
        self.reg_user.pack(pady=10)

        self.reg_email = ctk.CTkEntry(self.container, placeholder_text="Email", width=250, height=40)
        self.reg_email.pack(pady=10)

        self.reg_pass = ctk.CTkEntry(self.container, placeholder_text="Password", show="*", width=250, height=40)
        self.reg_pass.pack(pady=10)

        reg_btn = ctk.CTkButton(self.container, text="Sign Up", width=250, height=40, command=self.register_event)
        reg_btn.pack(pady=24)

        back_btn = ctk.CTkButton(self.container, text="Back to Login", fg_color="transparent", 
                                 hover_color="#333333", command=self.show_login)
        back_btn.pack()

    def login_event(self):
        print(f"Login attempt: {self.username.get()}")

    def register_event(self):
        print(f"Registering: {self.reg_user.get()}")

if __name__ == "__main__":
    app = App()
    app.mainloop()