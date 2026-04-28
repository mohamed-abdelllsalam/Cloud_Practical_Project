import tkinter as tk
import re
from tkinter import font, messagebox
from models import initialize_database, Account
from balance import balance_screen
from transfer import transfer_money_page
from donations import donations_screen
from withdraw import setup_withdraw_page
from deposite import setup_deposit_page
from change_currency import ChangeCurrencyFunc_Screen
from utils import root 
from PIL import ImageTk , Image
import os

initialize_database()  

image_path = r"images/bank.jpg"
if os.path.exists(image_path):
    image = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width-200}x{screen_height-100}")
    background_image = ImageTk.PhotoImage(image)

    # Set the background
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
else:
    print("File not found:", image_path)

withdraw_frame = tk.Frame(root)
deposit_frame = tk.Frame(root)

def closeWindow(event):
    root.destroy()

# Escape key to close the window
root.bind("<Escape>", closeWindow)

# Login state
is_logged_in = False  # Initially, the user is not logged in
current_account = None #hg

# Operation Buttons
def withdrawFunc():
    # Navigate to withdraw page
    setup_withdraw_page(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen)


def depositFunc():
    # Navigate to deposit page
    setup_deposit_page(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen)


def donationsFunc():
    donations_screen(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen)
   

def changeCurrencyFunc():
    ChangeCurrencyFunc_Screen(content_frame, is_logged_in, current_account, Account, update_screen, login_screen,operation_screen)


def myBalanceFunc():
    balance_screen(content_frame,is_logged_in, current_account, Account, update_screen, login_screen , operation_screen)


def transferMoneyFunc():
    transfer_money_page(content_frame, is_logged_in, current_account, Account, update_screen, login_screen,operation_screen)

def update_screen(content_fn):
    """Updates the content of the middle screen with the specified content function."""
    for widget in content_frame.winfo_children():
        widget.destroy()  # Clear the content frame
    content_fn()

# added by beshary
limitPassword = None
# limits password -> 12 chars
def limit_password_input(new_value):
    return len(new_value) <= 12

# Create validation command
limitPassword = root.register(limit_password_input)
def login_screen():
    global limitPassword
    # Title
    tk.Label(content_frame, text="Login", font=("Helvetica", 40)).grid(row=0, column=0, columnspan=2, pady=20)

    # Username
    tk.Label(content_frame, text="Username", font=("Helvetica", 20)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    loginUsername_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    loginUsername_entry.grid(row=1, column=1, padx=10, pady=10)

    # Password
    tk.Label(content_frame, text="Password", font=("Helvetica", 20)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
    loginPassword_entry = tk.Entry(content_frame, font=("Helvetica", 15), show="*" ,validate = "key" , validatecommand=(limitPassword, "%P"))
    loginPassword_entry.grid(row=2, column=1, padx=10, pady=10)

    # edited by beshary
    # Perform login function
    def perform_login():
        global is_logged_in
        global logged_id # added by Fatma 
        loginUsername = loginUsername_entry.get()  # Get username from entry field
        loginPassword = loginPassword_entry.get()  # Get password from entry field

        # Use the Account.login method to check credentials
        account = Account.login(loginUsername, loginPassword)

        if account:
            is_logged_in = True
            logged_id = account[1]  # account[1] = username
            messagebox.showinfo("Login Successful", f"Welcome {account[1]}!")
            update_screen(operation_screen)
            global current_account
            current_account = account
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


    # Login Button
    tk.Button(content_frame, text="Login", font=("Helvetica", 15), command=perform_login).grid(row=3, column=0, columnspan=2, pady=20)

    # Signup Button
    tk.Button(content_frame, text="Signup", font=("Helvetica", 15), command=lambda: update_screen(signup_screen)).grid(row=4, column=0, columnspan=2, pady=10)
def signup_screen():
    global limitPassword
    # Title
    tk.Label(content_frame, text="Signup", font=("Helvetica", 40)).grid(row=0, column=0, columnspan=2, pady=20)

    # Username
    tk.Label(content_frame, text="Username", font=("Helvetica", 20)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    username_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    username_entry.grid(row=1, column=1, padx=10, pady=10)

    # Password
    tk.Label(content_frame, text="Password", font=("Helvetica", 20)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
    password_entry = tk.Entry(content_frame, font=("Helvetica", 15), show="*" , validate = "key" , validatecommand=(limitPassword, "%P"))
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    # Email
    tk.Label(content_frame, text="Email", font=("Helvetica", 20)).grid(row=3, column=0, padx=10, pady=10, sticky='e')
    email_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    # Phone
    tk.Label(content_frame, text="Phone", font=("Helvetica", 20)).grid(row=4, column=0, padx=10, pady=10, sticky='e')
    phone_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    phone_entry.grid(row=4, column=1, padx=10, pady=10)

    # National ID
    tk.Label(content_frame, text="National ID", font=("Helvetica", 20)).grid(row=5, column=0, padx=10, pady=10, sticky='e')
    national_id_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    national_id_entry.grid(row=5, column=1, padx=10, pady=10)

    # Signup validation
    def validate_and_signup():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        national_id = national_id_entry.get()

        if not username or not password or not email or not phone or not national_id:
            messagebox.showerror("Input Error", "All fields must be filled.")
            return
        
        # added by beshary
        # username validation -> character  
        if not username.isalnum():
            messagebox.showerror("Input Error", "Invalid username format.")
            return
        elif len(username) > 12 or len(username) < 3:
            messagebox.showerror("Input Error", "Invalid username range between 3 and 12 character.")
            return
        
        # username validation -> uniqueness  
        if not Account.is_username_unique(username):
            messagebox.showerror("Input Error", "This username already exists.")
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  
            messagebox.showerror("Input Error", "Invalid email format.")
            return
        
        if not phone.isdigit() or len(phone) != 11:  
            messagebox.showerror("Input Error", "Phone number must be 11 digits.")
            return
        
        if not national_id.isdigit() or len(national_id) != 14:  
            messagebox.showerror("Input Error", "National ID must be 14 digits.")
            return
        
        # Validate password (at least 8 characters, 1 digit, 1 uppercase, 1 lowercase, 1 special char)
        password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$'
        if not re.match(password_regex, password):
            tk.messagebox.showerror("Input Error", "Password must be at least 8 characters long, contain at least one digit, one uppercase letter, one lowercase letter, and one special character.")
            return

        # If validation passes, create account
        if Account.create_account(username, password, email, phone, national_id):
            messagebox.showinfo("Signup Success", "Account created successfully!")
            update_screen(login_screen)  # Go back to login screen after successful signup
        else:
            messagebox.showerror("Signup Failed", "Account creation failed. Try a different username.")

    # Signup Button
    tk.Button(content_frame, text="Signup", font=("Helvetica", 15), command=validate_and_signup).grid(row=6, column=0, columnspan=2, pady=20)

def operation_screen():
    tk.Label(content_frame, text="Welcome to Your Dashboard", font=("Helvetica", 28)).pack(pady=20)
    content_frame.config(width=700, height=100, bg="white")
    content_frame.pack_propagate(False)  # Prevent resizing based on content
    content_frame.grid_propagate(False)  # Prevent resizing in grid layout


# added by fatma
def operation_detail(detail_text):
    if not is_logged_in:
        messagebox.showwarning("Access Denied", "You must log in first to perform this operation.")
        update_screen(login_screen)
        return
    tk.Label(content_frame, text=detail_text, font=("Helvetica", 20)).pack(pady=50)


# Home Page Label
text = "Welcome to BMS Bank"
labelFont = font.Font(family="Helvetica", size=40)
mainLabel = tk.Label(root, text=text, font=labelFont, bg="#000040", fg="white")
mainLabel.pack(pady=40)

# Frames
buttonFrameLeft = tk.Frame(root, bg="lightgray", width=200)
buttonFrameLeft.pack(side='left', fill='y')

content_frame = tk.Frame(root, bg="lightgray", width=1500, height=800)
content_frame.place(relx=0.5, rely=0.5, anchor="center")  
content_frame.pack_propagate(False)  # Prevent resizing based on child widgets


buttonFrameRight = tk.Frame(root, bg="lightgray", width=200)
buttonFrameRight.pack(side='right', fill='y')

# Left Buttons
buttonFont = font.Font(family="Arial", size=14, weight="bold")
buttons_left = [
    ("Transfer Money", transferMoneyFunc),
    ("My Balance", myBalanceFunc),
    ("Change Currency", changeCurrencyFunc),
]

for text, cmd in buttons_left:
    tk.Button(
        buttonFrameLeft, text=text, command=cmd,
        bg="gray", fg="white", activebackground="green", activeforeground="White",
        font=buttonFont, width=15, height=10
    ).pack(pady=5, padx=5)

# Right Buttons
buttons_right = [
    ("Withdraw", withdrawFunc),
    ("Deposit", depositFunc),
    ("Donate", donationsFunc),
]

for text, cmd in buttons_right:
    tk.Button(
        buttonFrameRight, text=text, command=cmd,
        bg="gray", fg="white", activebackground="green", activeforeground="White",
        font=buttonFont, width=15, height=10
    ).pack(pady=5, padx=5)

# Initialize Content Frame with Login Screen
update_screen(login_screen)

root.mainloop()