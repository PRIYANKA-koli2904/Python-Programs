import tkinter as tk
window = tk.Tk()

window.title("Welcome to Tkinter")
greeting = tk.Label(text="Hello, Tkinter")
lbl = tk.Label(window, text="Hello", font=("Arial Bold", 50))
lbl.pack()
greeting.pack()
window.mainloop()

