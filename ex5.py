import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry()

name = entry.get()
print(name)

label.pack()
entry.pack()

name = entry.get()
print(name)

