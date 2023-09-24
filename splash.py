import tkinter as tk
from tkinter import ttk
import time
from main import PasswordGeneratorApp  # Import your main application class

class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Splash Screen")
        self.root.geometry("800x600")

        self.bg_label = ttk.Label(root, background="#FF5733")
        self.bg_label.place(relwidth=1, relheight=1)

        self.logo_label = ttk.Label(root, text="Password Generator App", font=("Helvetica", 36), foreground="white", background="#FF5733")
        self.logo_label.pack(pady=200)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.progress_bar.pack(pady=10)

        self.loading_label = ttk.Label(root, text="Loading...", font=("Helvetica", 16), foreground="white", background="#FF5733")
        self.loading_label.pack()

        self.root.after(100, self.start_loading)

    def start_loading(self):
        for i in range(101):
            self.progress_bar["value"] = i
            self.root.update_idletasks()
            time.sleep(0.03)
        self.root.destroy()
        self.open_main_app()

    def open_main_app(self):
        main_window = tk.Tk()
        app = PasswordGeneratorApp(main_window)  # Create an instance of your main application class
        main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = SplashScreen(root)
    root.mainloop()
