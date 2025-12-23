import tkinter as tk
from tkinter import ttk
import string
import random


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

        self.run_btn = tk.Button(self.container, text="Select", command=self.handle_execution, bg="green", fg="white")
        self.run_btn.pack(pady=20)

    def handle_execution(self):
        choice = self.algorithm_choice.get()
        if choice == "RSA Encryption":
            # Switch to RSA View
            RSAView(self.container, self.show_main_menu)
        elif choice == "Fibonacci (DP)":
            FibonacciAlgorithmi(self.container, self.show_main_menu)
        elif choice == "Sorting (Bubble/Selection)":
            SortingAlgorithm(self.container, self.show_main_menu)


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

        tk.Label(self.parent, text="Enter Key leave blank for random Key").pack(pady=5)
        self.key_input = tk.Entry(self.parent, width=50)
        if self.key_input == "":
            # Source - https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
            # Posted by Ignacio Vazquez-Abrams, modified by community. See post 'Timeline' for change history
            # Retrieved 2025-12-23, License - CC BY-SA 4.0
            n = random.randint(1, 20)
            self.key_input = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
        self.user_input.pack(pady=5)

        # Action Buttons
        tk.Button(self.parent, text="Encrypt", command=self.encryption_Algorithm).pack(pady=5)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)

    def encryption_Algorithm(self):
        print(f"Processing: {self.user_input.get()}")


class FibonacciAlgorithmi:
    def __init__(self, parent, back_callback):
        self.parent = parent
        # Clear the menu to show RSA interface
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Fibonacci", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter number of steps in sequence").pack(pady=5)
        self.user_input = tk.Entry(self.parent)
        self.user_input.pack(pady=5)

        # Action Buttons
        tk.Button(self.parent, text="Calculate", command=self.solve).pack(pady=5)

        self.result_label = tk.Label(self.parent, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=20)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)


    def solve(self):#
        if self.user_input.get != '': n = int(self.user_input.get().strip())
        # Base cases
        if n < 0:
            return "Invalid Input"
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Initialize the DP table (array) with zeros
        # This is the "Tabulation" method
        fib_table = [0] * (n + 1)

        # Set base values
        fib_table[0] = 0
        fib_table[1] = 1

        # Fill the table iteratively
        for i in range(2, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        result = fib_table[n]

        self.result_label.config(text=f"Result: {result}")


class SortingAlgorithm:
    def __init__(self, parent, back_callback):
        self.parent = parent
        # Clear the menu to show RSA interface
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Sorting Algorithms", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter Comma seperated list").pack(pady=5)
        self.user_input = tk.Entry(self.parent, width=50)
        self.user_input.pack(pady=5)


        # Action Buttons
        tk.Button(self.parent, text="Bubble", command=self.BubbleAlgorithm).pack(padx=5, pady=5)
        tk.Button(self.parent, text="Selection", command=self.SelectionAlgorithm).pack(padx=10)

        self.sortOrder = ttk.Combobox(self.parent, values=["Ascending", "Descending"])
        self.sortOrder.pack(pady=5)

        self.result_label = tk.Label(self.parent, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=20)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)

    def BubbleAlgorithm(self):
        order = self.sortOrder.get()[0]
        self.input = [int(x.strip()) for x in self.user_input.get().split(',') if x.strip()]

        if order ==  "A":
            for j in range(len(self.input)):
                for i in range(len(self.input) - 1):
                    if self.input[i] > self.input[i + 1]:
                        temporaryNumber = int(self.input[i + 1])
                        self.input[i + 1] = self.input[i]
                        self.input[i] = temporaryNumber
        elif order == "D":
            for j in range(len(self.input)):
                for i in range(len(self.input) - 1):
                    if self.input[i] < self.input[i + 1]:
                        temporaryNumber = int(self.input[i + 1])
                        self.input[i + 1] = self.input[i]
                        self.input[i] = temporaryNumber

        self.result_label.config(text=f"Result: {self.input}")

    def SelectionAlgorithm(self):
        print(type(self.input))


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()