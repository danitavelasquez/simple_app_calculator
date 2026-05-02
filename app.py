# imports
import tkinter as tk
from ui import CalculatorUI

# base class for our app
class BaseApp:
    def __init__(self, title="App", size="500x500"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
    def run(self):
        self.root.mainloop()

# the main app
class CalculatorApp(BaseApp):
    def __init__(self):
        super().__init__(title="Simple Calculator", size="500x500")
        self.ui = CalculatorUI(self.root)