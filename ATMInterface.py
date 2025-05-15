import tkinter as tk
from tkinter import messagebox, simpledialog

class ATMApp:
    def __init__(self, master):
        self.master = master
        master.title("ATM Interface")
        master.geometry("300x350")
        self.correct_pin = "1234"
        self.balance = 5000.00

        self.login_screen()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Welcome to ATM", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.master, text="Enter your 4-digit PIN").pack(pady=5)
        self.pin_entry = tk.Entry(self.master, show="*", justify='center')
        self.pin_entry.pack()
        tk.Button(self.master, text="Login", command=self.check_pin).pack(pady=10)

    def check_pin(self):
        pin = self.pin_entry.get()
        if pin == self.correct_pin:
            self.main_menu()
        else:
            messagebox.showerror("Error", "Incorrect PIN!")

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.master, text="ATM Main Menu", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.master, text="Check Balance", width=20, command=self.check_balance).pack(pady=5)
        tk.Button(self.master, text="Deposit", width=20, command=self.deposit).pack(pady=5)
        tk.Button(self.master, text="Withdraw", width=20, command=self.withdraw).pack(pady=5)
        tk.Button(self.master, text="Exit", width=20, command=self.master.quit).pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
            if amount is None:
                return
            if amount <= 0:
                messagebox.showerror("Error", "Enter a valid amount.")
            else:
                self.balance += amount
                messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully.")
        except:
            messagebox.showerror("Error", "Invalid input.")

    def withdraw(self):
        try:
            amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
            if amount is None:
                return
            if amount <= 0:
                messagebox.showerror("Error", "Enter a valid amount.")
            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully.")
        except:
            messagebox.showerror("Error", "Invalid input.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
