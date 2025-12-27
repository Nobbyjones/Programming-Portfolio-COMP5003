import tkinter as tk
from tkinter import ttk
import string
import random
from turtledemo.sorting_animate import randomize


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
            "Shuffle Deck",
            "Factorial",
            "Search",
            "Palindrome Counter"
        ], width=40)
        self.algorithm_choice.pack(pady=10)

        self.run_btn = tk.Button(self.container, text="Select", command=self.handle_execution, bg="green", fg="white")
        self.run_btn.pack(pady=20)

    def handle_execution(self):
        choice = self.algorithm_choice.get()

        # Use the Factory to create the view
        # We don't need if/elif anymore!
        view = AlgorithmFactory.create_view(
            choice,
            self.container,
            self.show_main_menu
        )

        if not view:
            print(f"Error: Logic for {choice} not found.")


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

        tk.Label(self.parent, text="Enter Key to Encrypt/Decrypt With, (leave blank for random Key):").pack(pady=5)
        self.user_key = tk.Entry(self.parent, width=50)
        self.user_key.pack(pady=5)


        # Action Buttons
        tk.Button(self.parent, text="Encrypt", command=self.encryption_Algorithm).pack(pady=5)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)

    def encryption_Algorithm(self):
        if self.user_key.get() == "":
            # Source - https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
            n = random.randint(1, 20)
            self.key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
        else:
            self.key = self.user_key.get()

        print(f"Key: {self.key}")
        print(f"Input: {self.user_input.get()}")


class FibonacciAlgorithm:
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
        if order == "": order = "A"
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
        order = self.sortOrder.get()[0]
        if order == "": order = "A"
        self.input = [int(x.strip()) for x in self.user_input.get().split(',') if x.strip()]
        n = len(self.input)

        for i in range(n):
            extreme_index = i

            for j in range(i + 1, n):
                if order == "A":
                    if self.input[j] < self.input[extreme_index]:
                        extreme_index = j
                else:
                    if self.input[j] > self.input[extreme_index]:
                        extreme_index = j

            if extreme_index != i:
                self.input[i], self.input[extreme_index] = self.input[extreme_index], self.input[i]

        self.result_label.config(text=f"Result: {self.input}")


class MergeSort:
    def __init__(self, parent, back_callback):
        self.parent = parent
        # Clear the menu to show RSA interface
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Divide and Conquer", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter Comma seperated list").pack(pady=5)
        self.user_input = tk.Entry(self.parent, width=50)
        self.user_input.pack(pady=5)

        self.sortOrder = ttk.Combobox(self.parent, values=["Ascending", "Descending"])
        self.sortOrder.pack(pady=5)
        array = []
        order  = ""


        # Action Buttons
        tk.Button(self.parent, text="Sort", command=lambda: self.sort(array, order)).pack(padx=10)



        self.result_label = tk.Label(self.parent, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=20)

        # Navigation Button
        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=20)

    def sort(self, array, order):
        #This try was from gemini to fix a bug, remember to note in write up
        if not array:
            try:
                order = self.sortOrder.get()[0] if self.sortOrder.get() else "A"
                array = [int(x.strip()) for x in self.user_input.get().split(',') if x.strip()]
            except (ValueError, IndexError):
                self.result_label.config(text="Error: Invalid Input")
                return

        n = len(array)

        if n <= 1:
            return array

        mid = n // 2
        left_half = array[:mid]
        right_half = array[mid:]

        left_sorted = self.sort(left_half, order)
        right_sorted = self.sort(right_half, order)

        final_merge = self.merge(left_sorted, right_sorted, order)

        self.result_label.config(text=f"Result: {final_merge}")

        return final_merge

    def merge(self, left, right, order):
        sorted_array = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if order == "A":
                condition = left[i] <= right[j]
            else:
                condition = left[i] >= right[j]

            if condition:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array


class DeckShuffle:
    def __init__(self, parent, back_callback):
        self.parent = parent
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Randomized Deck Shuffle", font=("Arial", 18, "bold")).pack(pady=10)

        # Action Button
        tk.Button(self.parent, text="Shuffle New Deck", command=self.display_shuffle, bg="blue", fg="white").pack(
            pady=10)

        # https://www.geeksforgeeks.org/python/python-tkinter-text-widget/
        self.result_area = tk.Text(self.parent, height=12, width=50)
        self.result_area.pack(pady=10)

        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=10)

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [f"{v} of {s}" for s in suits for v in values]

    def shuffle(self, deck):
        # https://www.geeksforgeeks.org/dsa/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
        # Implementation from scratch
        n = len(deck)
        for i in range(n - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i)
            # Swap deck[i] with the element at random index
            deck[i], deck[j] = deck[j], deck[i]
        return deck

    def display_shuffle(self):
        deck = self.create_deck()
        shuffled_deck = self.shuffle(deck)

        self.result_area.delete('1.0', tk.END)
        for i, card in enumerate(shuffled_deck, 1):
            self.result_area.insert(tk.END, f"{i}. {card}\n")


class FactorialRecursion:
    def __init__(self, parent, back_callback):
        self.parent = parent
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Recursive Factorial", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter a non-negative integer:").pack(pady=5)
        self.user_input = tk.Entry(self.parent)
        self.user_input.pack(pady=5)

        tk.Button(self.parent, text="Calculate", command=self.run_factorial, bg="purple", fg="white").pack(pady=10)

        self.result_label = tk.Label(self.parent, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=20)

        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=10)

    def calculate_factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

    def run_factorial(self):
        val = self.user_input.get().strip()
        try:
            n = int(val)
            if n < 0:
                self.result_label.config(text="Error: Enter a positive number")
            elif n > 992:
                self.result_label.config(text="Error: Number too large for recursion")
            else:
                result = self.calculate_factorial(n)
                self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Error: Invalid input")


class SearchStatistics:
    def __init__(self, parent, back_callback):
        self.parent = parent
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Array Statistics", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter numbers separated by commas:").pack()
        self.user_input = tk.Entry(self.parent, width=50)
        self.user_input.pack(pady=5)

        tk.Button(self.parent, text="Calculate Stats", command=self.process_stats).pack(pady=10)

        # Result display area
        self.result_box = tk.Label(self.parent, text="", justify="left", font=("Courier", 10))
        self.result_box.pack(pady=10)

        tk.Button(self.parent, text="Back", command=back_callback).pack()

    def calculate_mode(self, arr):
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        return modes if len(modes) < len(arr) else "No unique mode"

    def get_percentile(self, sorted_arr, percentile):
        """ Calculates values at specific positions (Median, Q1, Q3) """
        n = len(sorted_arr)
        index = percentile * (n - 1)
        lower = int(index)
        upper = lower + 1

        if upper >= n:
            return sorted_arr[lower]

        # Linear interpolation for more accurate quartiles
        weight = index - lower
        return sorted_arr[lower] * (1 - weight) + sorted_arr[upper] * weight

    def process_stats(self):
        raw_data = self.user_input.get()
        # 1. Parse and Sort the data (Crucial for Median/Quartiles)
        data = sorted([int(x.strip()) for x in raw_data.split(',') if x.strip()])

        if not data: return

        # 2. Calculations
        smallest = data[0]
        largest = data[-1]
        mode = self.calculate_mode(data)
        median = self.get_percentile(data, 0.5)
        q1 = self.get_percentile(data, 0.25)
        q3 = self.get_percentile(data, 0.75)

        # 3. Display
        res = (f"Smallest: {smallest}\n"
                f"Largest:  {largest}\n"
                f"Mode:     {mode}\n"
                f"Median:   {median:.2f}\n"
                f"1st Q (Q1): {q1:.2f}\n"
                f"3rd Q (Q3): {q3:.2f}")
        self.result_box.config(text=res)


class PalindromeCounter:
    def __init__(self, parent, back_callback):
        self.parent = parent
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Palindrome Substring Counter", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.parent, text="Enter a string:").pack(pady=5)
        self.user_input = tk.Entry(self.parent, width=40)
        self.user_input.pack(pady=5)

        tk.Button(self.parent, text="Count Palindromes", command=self.run_logic, bg="teal", fg="white").pack(pady=10)

        self.result_label = tk.Label(self.parent, text="Total Palindromes: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Area to show which substrings were found
        self.found_area = tk.Text(self.parent, height=8, width=40)
        self.found_area.pack(pady=10)

        tk.Button(self.parent, text="Back to Menu", command=back_callback).pack(pady=10)

    def run_logic(self):
        s = self.user_input.get().strip()
        if not s: return ""

        n = len(s)
        # Memoization table: memo[i][j] will be True if s[i...j] is a palindrome
        memo = [[False] * n for _ in range(n)]
        count = 0
        palindromes_found = []

        # Substrings of length 1 (Single letters are always palindromes)
        for i in range(n):
            memo[i][i] = True
            count += 1
            palindromes_found.append(s[i])

        # Substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = True
                count += 1
                palindromes_found.append(s[i:i + 2])

        # Substrings of length 3 or more
        # k is the length of the substring
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1  # Ending index

                # Check if outer characters match AND inner part is a palindrome
                if s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True
                    count += 1
                    palindromes_found.append(s[i:j + 1])

        # Update GUI
        self.result_label.config(text=f"Total Palindromes: {count}")
        self.found_area.delete('1.0', tk.END)
        self.found_area.insert(tk.END, ", ".join(palindromes_found))


class AlgorithmFactory:
    # Requirement 10 Creational Design Pattern
    # https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/

    @staticmethod
    def create_view(choice, parent, back_callback):
        # A dictionary mapping choices to class names
        # This is much cleaner than a 10-line if/elif block
        views = {
            "RSA Encryption": RSAView,
            "Fibonacci (DP)": FibonacciAlgorithm,
            "Sorting (Bubble/Selection)": SortingAlgorithm,
            "Merge Sort (Divide & Conquer)": MergeSort,
            "Shuffle Deck": DeckShuffle,
            "Factorial": FactorialRecursion,
            "Search": SearchStatistics,
            "Palindrome Counter": PalindromeCounter
        }

        view_class = views.get(choice)

        if view_class:
            # Instantiate and return the object
            return view_class(parent, back_callback)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()