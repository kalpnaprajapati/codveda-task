import tkinter as tk
import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < target_number:
            result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > target_number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            result_label.config(text=f"Congratulations! {guess} is correct.", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="black")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create and place widgets
instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Check", command=check_guess)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
