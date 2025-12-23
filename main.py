import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Workshop")
        self.root.geometry("600x500")

        # Container to hold current view
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.show_main_menu()

    def clear_window(self):
        """Removes all widgets from the container frame."""
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        tk.Label(self.container, text="Algorithm Toolset", font=("Arial", 18, "bold")).pack(pady=10)

        # Selection Menu
        self.algorithm_choice = ttk.Combobox(self.container, values=[
            "RSA Encryption",
            "Fibonacci (DP)",
            "Sorting (Bubble/Selection)",
            "Merge Sort (Divide & Conquer)",
            "Palindrome Counter (DP/Memo)",
            "Shuffle Deck"
        ], width=40)
        self.algorithm_choice.pack(pady=10)

        self.run_btn = tk.Button(self.container, text="Execute", command=self.handle_execution, bg="green", fg="white")
        self.run_btn.pack(pady=20)

    def handle_execution(self):
        choice = self.algorithm_choice.get()
        if choice == "RSA Encryption":
            # Switch to RSA View
            RSAView(self.container, self.show_main_menu)


class RSAView:
    def __init__(self, parent, back_callback):
        self.parent = parent
        # Clear the menu to show RSA interface
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="RSA Encryption Module", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter Message to Encrypt/Decrypt:").pack(pady=5)
        self.user_input = tk.Entry(self.parent, width=50)
        self.user_input.pack(pady=5)

        # Action Buttons
        tk.Button(self.parent, text="Encrypt", command=self.placeholder_action).pack(pady=5)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)

    def placeholder_action(self):
        print(f"Processing: {self.user_input.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()