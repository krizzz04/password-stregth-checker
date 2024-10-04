import tkinter as tk
from tkinter import messagebox
import re

# Function to check the complexity of the password
def assess_password_strength(password):
    complexity_score = 0
    feedback = []

    # Criteria 1: Check length
    if len(password) >= 8:
        complexity_score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Criteria 2: Check for uppercase letters
    if re.search(r'[A-Z]', password):
        complexity_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Criteria 3: Check for lowercase letters
    if re.search(r'[a-z]', password):
        complexity_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Criteria 4: Check for numbers
    if re.search(r'[0-9]', password):
        complexity_score += 1
    else:
        feedback.append("Include at least one number.")

    # Criteria 5: Check for special characters
    if re.search(r'[\W_]', password):
        complexity_score += 1
    else:
        feedback.append("Include at least one special character.")

    # Feedback on overall password strength
    if complexity_score == 5:
        feedback.append("Strength: Strong 💪")
    elif complexity_score >= 3:
        feedback.append("Strength: Moderate ⚠️")
    else:
        feedback.append("Strength: Weak ❌")

    return feedback

# GUI application for password complexity check
class HackerPasswordChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity - Mr. Robot Theme")
        self.root.geometry("500x400")
        self.root.config(bg='#0d0d0d')  # Dark background for hacker theme
        
        self.font_style = ("Courier", 12)
        self.text_color = "#00FF00"  # Neon green for hacker-like text
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Enter Your Password", font=("Courier", 16), fg="#FF0000", bg='#0d0d0d').pack(pady=10)

        # Password Entry Field
        self.password_entry = tk.Entry(self.root, font=self.font_style, fg='#00FF00', bg='#1c1c1c', insertbackground='#FF0000', show="*")
        self.password_entry.pack(pady=10)

        # Check Password Button
        self.check_button = tk.Button(self.root, text="Check Password", font=self.font_style, fg=self.text_color, bg='#333333', command=self.check_password)
        self.check_button.pack(pady=10)

        # Feedback Area
        self.feedback_label = tk.Label(self.root, text="", font=self.font_style, fg=self.text_color, bg='#0d0d0d')
        self.feedback_label.pack(pady=20)

    def check_password(self):
        password = self.password_entry.get()
        feedback = assess_password_strength(password)
        
        # Display feedback in a hacker style
        feedback_text = "\n".join(feedback)
        self.feedback_label.config(text=feedback_text)

        # Optional: Popup message for password strength
        if "Weak" in feedback_text:
            messagebox.showwarning("Password Strength", "Your password is weak! Improve it.")
        elif "Moderate" in feedback_text:
            messagebox.showinfo("Password Strength", "Your password is moderate. Could be stronger!")
        else:
            messagebox.showinfo("Password Strength", "Your password is strong. Good job!")

# Main function to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HackerPasswordChecker(root)
    root.mainloop()
