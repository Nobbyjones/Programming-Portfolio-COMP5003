import tkinter as tk
from tkinter import messagebox, ttk
import random

class mainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Workshop")
        self.root.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Algorithm Toolset", font=("Arial", 18, "bold")).pack(pady=10)

        # Selection Menu
        self.algo_choice = ttk.Combobox(self.root, values=[
            "RSA Encryption",
            "Fibonacci (DP)",
            "Sorting (Bubble/Selection)",
            "Merge Sort (Divide & Conquer)",
            "Palindrome Counter (DP/Memo)",
            "Shuffle Deck"
        ], width=40)
        self.algo_choice.pack(pady=10)

        self.input_label = tk.Label(self.root, text="Enter Input:")
        self.input_label.pack()
        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.pack(pady=5)

        self.run_btn = tk.Button(self.root, text="Execute", command=self.run_algorithm, bg="green", fg="white")
        self.run_btn.pack(pady=20)

        self.result_area = tk.Text(self.root, height=10, width=60)
        self.result_area.pack(pady=10)

    def run_algorithm(self):
        choice = self.algo_choice.get()
        data = self.user_input.get()
        self.result_area.delete('1.0', tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()