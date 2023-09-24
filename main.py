import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.dark_mode = False  # Flag for toggling dark mode

        self.heading_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"))
        self.heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.words_label = ttk.Label(root, text="Enter Words (comma-separated):", font=("Helvetica", 14))
        self.words_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.words_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.words_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        self.include_special_var = tk.IntVar()
        self.include_special_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=self.include_special_var)
        self.include_special_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.password_length_label = ttk.Label(root, text="Password Length:", font=("Helvetica", 14))
        self.password_length_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.password_length_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.password_length_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")
        self.password_length_entry.insert(0, "12")  # Default password length

        self.toggle_dark_mode_button = ttk.Button(root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.toggle_dark_mode_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        self.style.configure("TButton", font=("Helvetica", 14))

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.history_label = ttk.Label(root, text="Password History:", font=("Helvetica", 14))
        self.history_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.history_text = tk.Text(root, font=("Helvetica", 12), height=6, wrap=tk.WORD)
        self.history_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.style.theme_use("clam")
            self.root.configure(bg="#333333")
        else:
            self.style.theme_use("clam")
            self.root.configure(bg="white")

    def generate_password(self):
        words = self.words_entry.get().split(',')
        random.shuffle(words)

        password_length = int(self.password_length_entry.get())
        character_pool = string.ascii_letters + string.digits
        if self.include_special_var.get():
            character_pool += string.punctuation

        password = ''.join(random.choice(character_pool) for _ in range(password_length - len(words)))

        self.result_label.config(text=f"Generated Password: {''.join(words)}{password}")
        self.copy_password(''.join(words) + password)
        self.add_to_history(password)

    def copy_password(self, password):
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()

    def add_to_history(self, password):
        current_history = self.history_text.get("1.0", tk.END).strip()
        if current_history:
            new_history = current_history + "\n" + password
        else:
            new_history = password

        self.history_text.delete("1.0", tk.END)
        self.history_text.insert("1.0", new_history)
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
