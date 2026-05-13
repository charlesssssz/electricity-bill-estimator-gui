import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Electricity Bill Estimator")

title = ttk.Label(root, text="Electricity Bill Estimator", font="helvetica 16 bold  ")
title.pack()

frame1 = ttk.LabelFrame(root, text="Manual Calculation")
frame1.pack()
ttk.Label(frame1, text="kWh Used").grid(row=0, column=0)
entry_kwh = ttk.Entry(frame1)
entry_kwh.grid(row=0, column=1)

def test():
    print("Button clicked")

ttk.Button(frame1, text="Calculate", command=test).grid(row=1, columnspan=2, pady=5)    

root.mainloop()