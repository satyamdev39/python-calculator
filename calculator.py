import tkinter as tk

# Create window
window = tk.Tk()
window.title("Python Calculator")
window.geometry("350x450")
window.resizable(False, False)

# Display box
display = tk.Entry(window, font=("Arial", 20), borderwidth=5, justify="right")
display.pack(fill="x", padx=10, pady=10)

# Functions
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2)
]

frame = tk.Frame(window)
frame.pack()

for text, row, col in buttons:
    button = tk.Button(
        frame,
        text=text,
        width=6,
        height=2,
        font=("Arial", 14),
        command=lambda t=text: click(t)
    )
    button.grid(row=row, column=col, padx=5, pady=5)

# Equal button
equal = tk.Button(
    frame,
    text="=",
    width=6,
    height=2,
    font=("Arial", 14),
    command=calculate
)
equal.grid(row=3, column=3, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(
    window,
    text="Clear",
    width=20,
    height=2,
    font=("Arial", 14),
    command=clear
)
clear_btn.pack(pady=10)

window.mainloop()