import tkinter as tk
window = tk.Tk()
entry = tk.Entry(fg="white", bg="purple", width=50)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
entry.pack()
button.pack()
