import tkinter as tk
import random

# Function to check the guess
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

# Function to count words
def count_words():
    text = word_entry.get()
    word_count = len(text.split())
    count_label.config(text=f"Word Count: {word_count}")

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game & Word Counter")

# Number guessing section
instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Check", command=check_guess)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Word count section
word_label = tk.Label(root, text="Enter text for word count:")
word_label.pack()

word_entry = tk.Entry(root)
word_entry.pack()

count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

count_label = tk.Label(root, text="")
count_label.pack()

# Start the GUI event loop
root.mainloop()
