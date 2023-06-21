from tkinter import *
import string
import random


class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")

        # Create length label and entry
        self.label_length = Label(window, text="Length:")
        self.label_length.grid(row=0, column=0, padx=5, pady=5)
        self.entry_length = Entry(window)
        self.entry_length.grid(row=0, column=1, padx=5, pady=5)
        self.entry_length.insert(0, "8")  # Default to 8 characters

        # Create include capitals checkbox
        self.include_caps = BooleanVar()
        self.include_caps.set(True)  # Default to including digits
        self.checkbutton_digits = Checkbutton(window, text="Include caps", variable=self.include_caps)
        self.checkbutton_digits.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Create include digits checkbox
        self.include_digits = BooleanVar()
        self.include_digits.set(True)  # Default to including digits
        self.checkbutton_digits = Checkbutton(window, text="Include Digits", variable=self.include_digits)
        self.checkbutton_digits.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Create include special characters checkbox
        self.include_special_chars = BooleanVar()
        self.include_special_chars.set(False)  # Default to excluding special characters
        self.checkbutton_special_chars = Checkbutton(window, text="Include Special Characters",
                                                     variable=self.include_special_chars)
        self.checkbutton_special_chars.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Create generate button
        self.button_generate = Button(window, text="Generate", command=self.generate_password)
        self.button_generate.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Create password display label
        self.label_password = Label(window, text="Generated Password:")
        self.label_password.grid(row=5, column=0, padx=5, pady=5)
        self.entry_password = Entry(window, state="readonly")
        self.entry_password.grid(row=5, column=1, padx=5, pady=5)

    def generate_password(self):
        length = int(self.entry_length.get())
        include_caps = self.include_caps.get()
        include_digits = self.include_digits.get()
        include_special_chars = self.include_special_chars.get()

        characters = string.ascii_lowercase
        if include_caps:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.entry_password.configure(state="normal")
        self.entry_password.delete(0, END)
        self.entry_password.insert(0, password)
        self.entry_password.configure(state="readonly")


# Create the main window
window = Tk()

# Create an instance of the PasswordGenerator class
password_generator = PasswordGenerator(window)

# Start the main event loop
window.mainloop()
