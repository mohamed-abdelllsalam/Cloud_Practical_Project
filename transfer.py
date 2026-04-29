import tkinter as tk
from tkinter import messagebox


def transfer_money_page(content_frame, is_logged_in, current_account, Account, update_screen, login_screen, operation_screen):
    """
    Displays the transfer money page for the logged-in user.

    Args:
        content_frame: The Tkinter frame where the content is displayed.
        is_logged_in: Boolean indicating whether a user is logged in.
        current_account: Tuple containing details of the currently logged-in user.
        Account: The Account model for interacting with account-related methods.
        update_screen: Function to update the screen content.
        login_screen: The login screen function to redirect unauthorized users.
    """
    if not is_logged_in or not current_account:
        messagebox.showwarning("Access Denied", "You must log in first to perform this operation.")
        update_screen(login_screen)
        return

    # Clear previous content in the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Customize content_frame size and styling
    content_frame.config(width=800, height=330)
    content_frame.pack_propagate(False)  # Prevent resizing based on content
    content_frame.grid_propagate(False)  # Prevent resizing in grid layout

    # Add a title
    title_label = tk.Label(
        content_frame,
        text="Transfer Money",
        font=("Helvetica", 30, "bold"),
        fg="black"
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Recipient's name label and entry
    recipient_label = tk.Label(
        content_frame,
        text="Recipient's Name:",
        font=("Helvetica", 16),
        bg="white",
        anchor="w"
    )
    recipient_label.grid(row=1, column=0, sticky="w", padx=20, pady=10)

    recipient_name_entry = tk.Entry(content_frame, font=("Helvetica", 14), width=30)
    recipient_name_entry.grid(row=1, column=1, padx=20, pady=10)

    # Transfer amount label and entry
    amount_label = tk.Label(
        content_frame,
        text="Transfer Amount:",
        font=("Helvetica", 16),
        bg="white",
        anchor="w"
    )
    amount_label.grid(row=2, column=0, sticky="w", padx=20, pady=10)

    amount_entry = tk.Entry(content_frame, font=("Helvetica", 14), width=30)
    amount_entry.grid(row=2, column=1, padx=20, pady=10)

    # Handle transfer logic
    def handle_transfer():
        recipient_name = recipient_name_entry.get()  # Get the recipient's name
        amount = amount_entry.get()  # Get the transfer amount

        if recipient_name and amount:
            try:
                amount = float(amount)  # Convert amount to float

                # Check if amount is positive
                if amount <= 0:
                    messagebox.showerror("Invalid Amount", "Amount must be a positive number.")
                    return

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")
                return

            # Find recipient account by name
            recipient_account = Account.find_account_by_name(recipient_name)

            if recipient_account:
                recipient_id = recipient_account[0]  # Get recipient's account id
                sender_id = current_account[0]  # Get logged-in sender's account id

                # Deduct from sender's balance
                sender_balance_update = Account.update_account_balance(sender_id, -amount)
                if not sender_balance_update["success"]:
                    messagebox.showerror("Transfer Failed", sender_balance_update["message"])
                    return

                # Add to recipient's balance
                recipient_balance_update = Account.update_account_balance(recipient_id, amount)
                if not recipient_balance_update["success"]:
                    messagebox.showerror("Transfer Failed", recipient_balance_update["message"])
                    return

                # Log the transaction
                Account.log_transaction("Transfer", amount, sender_id, recipient_id)

                messagebox.showinfo("Transfer Successful", f"Transferred {amount} to {recipient_name} successfully!")
                update_screen(operation_screen)
            else:
                messagebox.showerror("Transfer Failed", "Recipient not found!")
        else:
            messagebox.showerror("Transfer Failed", "Please enter both recipient name and amount.")

    # Add a Send button
    send_button = tk.Button(
        content_frame,
        text="Send",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="green",
        fg="white",
        activebackground="darkgreen",
        activeforeground="white",
        command=handle_transfer
    )
    send_button.grid(row=3, column=0, columnspan=2, pady=30)

    # Add some spacing for better layout
    content_frame.grid_rowconfigure(4, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=1)
