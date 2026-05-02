# imports
import tkinter as tk
from tkinter import messagebox
from operations import Addition, Subtraction, Multiplication, Division

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        # map operation for classes
        self.operation_map = {
            "Addition": Addition(),
            "Subtraction": Subtraction(),
            "Multiplication": Multiplication(),
            "Division": Division()
        }
        # what value user selected
        self.selected_operation = tk.StringVar(value="Addition")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Select operation:").pack(pady=5)
        for op in self.operation_map:
            tk.Radiobutton(
                self.root,
                text=op,
                variable=self.selected_operation,
                value=op
            ).pack(anchor="w")
        # input for first number
        tk.Label(self.root, text="Enter first number:").pack(pady=5)
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        # input for second number
        tk.Label(self.root, text="Enter second number:").pack(pady=5)
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()
        # buttons
        tk.Button(self.root, text="Calculate", command=self.calculate).pack(pady=10)
        tk.Button(self.root, text="AC", command=self.reset).pack()
        # results
        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack(pady=10)

    def calculate(self):
        try: # inputs to numbers
            first_num = float(self.entry1.get())
            second_num = float(self.entry2.get())
            # operation to compute result
            operation = self.operation_map[self.selected_operation.get()]
            result = operation.calculate(first_num, second_num)
            self.result_label.config(text=f"Result: {result}")
            # try again message
            retry = messagebox.askyesno("Try Again", "Do you want to try again?")
            if not retry:
                messagebox.showinfo("Exit", "Thank you!")
                self.root.quit()
            else:
                self.reset()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")
        except ZeroDivisionError as e:
            messagebox.showerror("Operation Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    # clear inouts and result
    def reset(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Result: ")