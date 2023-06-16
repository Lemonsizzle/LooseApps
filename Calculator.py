from tkinter import *


class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")

        # Create the input field
        self.entry = Entry(window)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create number buttons
        numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        row = 1
        col = 0
        for number in numbers:
            button = Button(window, text=number, width=5, command=lambda num=number: self.append_input(num))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Create operator buttons
        operators = ['+', '-', '*', '/']
        row = 1
        col = 3
        for operator in operators:
            button = Button(window, text=operator, width=5, command=lambda op=operator: self.append_input(op))
            button.grid(row=row, column=col, padx=5, pady=5)
            row += 1

        # Create the clear button
        clear_button = Button(window, text="C", width=5, command=self.clear_input)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

        # Create the equals button
        equals_button = Button(window, text="=", width=5, command=self.calculate)
        equals_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    def append_input(self, value):
        self.entry.insert(END, value)

    def clear_input(self):
        self.entry.delete(0, END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, END)
            self.entry.insert(END, result)
        except (SyntaxError, ZeroDivisionError):
            self.entry.delete(0, END)
            self.entry.insert(END, "Error")


# Create the main window
window = Tk()

# Create an instance of the Calculator class
calculator = Calculator(window)

# Start the main event loop
window.mainloop()
