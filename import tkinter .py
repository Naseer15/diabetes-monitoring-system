import tkinter as tk
from tkinter import messagebox, simpledialog

# User data
users = {
    "Sara Norman": {
        "patient_name": "Sara Norman",  # Added patient_name
        "patient_id": "5344-9709",
        "doctor_name": "Dr. Jason Rosenberg",
        "doctor_phone": "579-0432",
        "low_glucose": 80,
        "normal_glucose": (80, 140),
        "high_glucose": 140
    },
    "Gregg Norman": {
        "patient_name": "Gregg Norman",  # Added patient_name
        "patient_id": "1275-4307",
        "doctor_name": "Dr. Nikhil Singh",
        "doctor_phone": "334-2309",
        "low_glucose": 70,
        "normal_glucose": (70, 120),
        "high_glucose": 120
    }
}

class DiabetesMonitoringSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diabetes Monitoring System")
        self.geometry("400x300")
        self.current_user = None

        # Login screen
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Select User:").pack()
        self.user_var = tk.StringVar()
        user_dropdown = tk.OptionMenu(self.login_frame, self.user_var, *users.keys())
        user_dropdown.pack(pady=10)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.pack()

        self.help_button = tk.Button(self, text="Help", command=self.show_help)
        self.help_button.pack(side=tk.BOTTOM, pady=10)

    def login(self):
        user_name = self.user_var.get()
        if user_name in users:
            self.current_user = users[user_name]
            self.login_frame.pack_forget()
            self.show_main_screen()
        else:
            messagebox.showerror("Error", "Invalid user selection.")

    def show_main_screen(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=20)

        tk.Label(self.main_frame, text=f"Welcome, {self.current_user['patient_name']}").pack(pady=10)  # Display patient_name
        tk.Label(self.main_frame, text=f"Patient ID: {self.current_user['patient_id']}").pack(pady=5)

        self.glucose_var = tk.IntVar()
        self.glucose_entry = tk.Entry(self.main_frame, textvariable=self.glucose_var)
        self.glucose_entry.pack(pady=10)

        glucose_button = tk.Button(self.main_frame, text="Record Glucose Reading", command=self.record_glucose)
        glucose_button.pack(pady=10)

        logout_button = tk.Button(self.main_frame, text="Logout", command=self.logout)
        logout_button.pack(pady=10)

    def record_glucose(self):
        glucose_reading = self.glucose_var.get()
        if glucose_reading == 0:
            messagebox.showwarning("Warning", "Please take your blood sugar reading and enter the value.")
            return

        low_glucose = self.current_user['low_glucose']
        normal_glucose = self.current_user['normal_glucose']
        high_glucose = self.current_user['high_glucose']

        if glucose_reading < low_glucose:
            messagebox.showwarning("Low Glucose Reading", f"Your glucose reading of {glucose_reading} is low. Please eat a sugar source, take your medicine, and eat meals and snacks as described by your doctor.")
            reason = simpledialog.askstring("Reason", "Please explain why you think your reading is low.")
        elif low_glucose <= glucose_reading <= high_glucose:
            messagebox.showinfo("Normal Glucose Reading", f"Your glucose reading of {glucose_reading} is within the normal range.")
        else:
            messagebox.showwarning("High Glucose Reading", f"Your glucose reading of {glucose_reading} is high. Please call your doctor {self.current_user['doctor_name']} at {self.current_user['doctor_phone']} immediately.")
            ketones = messagebox.askyesno("Ketones", "Do you have ketones in your urine?")
            reason = simpledialog.askstring("Reason", "Please explain why you think your reading is high.")

    def logout(self):
        self.main_frame.pack_forget()
        self.login_frame.pack(pady=20)  # Show the login screen after logging out
        self.user_var.set("")  # Clear the selected user

    def show_help(self):
        help_text = "This is the Diabetes Monitoring System. \n\n" \
                    "Login Screen:\n" \
                    "Select your name from the dropdown menu and click 'Login'.\n\n" \
                    "Main Screen:\n" \
                    "1. Enter your blood glucose reading in the entry box.\n" \
                    "2. Click 'Record Glucose Reading' to submit your reading.\n" \
                    "3. The system will provide feedback based on your reading.\n" \
                    "4. Click 'Logout' to return to the login screen."
        messagebox.showinfo("Help", help_text)

if __name__ == "__main__":
    app = DiabetesMonitoringSystem()
    app.mainloop()
