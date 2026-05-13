"""
Electricity Bill Estimator GUI System

This program is a Tkinter-based application that helps users estimate electricity bills.

It allows users to:
- Compute electricity bills manually using kWh and rate input
- Add appliances with power consumption details (watts, hours per day, days used)
- View a list of added appliances with their computed kWh usage
- Delete selected appliances or remove all saved appliances from the list
- Calculate total electricity consumption and estimated bill based on all appliances
- Save appliance data to a file and load it on program startup

The system uses a simple file-based storage (appliances.txt) to persist data between sessions.
"""
import tkinter as tk
from tkinter import ttk, messagebox

from file_handler import load_from_file, save_to_file

#MAIN DATA
#auto-load sha ng appliances mula sa file pag start ng program
appliances = load_from_file()

#FUNCTIONS
def manual_calculation():
    try:
        #kukunin yung input ng user
        kwh = float(entry_kwh.get())
        rate = float(entry_rate.get())

        #validation lang para iwas negative values because hindi valid yorn hahahah
        if kwh < 0 or rate < 0:
            messagebox.showerror("Error", "No negative values allowed!")
            return

        #simple manual compute langs ng bill ganern hahaha
        total = kwh * rate

        #display result
        result_label.config(text=f"Manual Bill: ₱{total:.2f}")

    except ValueError: 
        messagebox.showerror("Error", "Enter valid numbers only")

def add_appliance():
    try:
        #kuha ulit inputs ng user
        name = entry_name.get().strip()
        power = float(entry_power.get())
        hours = float(entry_hours.get())
        days = float(entry_days.get())

        #validation again and again hahahhaa
        if name == "":
            messagebox.showerror("Error", "Name is required!")
            return

        if power < 0 or hours < 0 or days < 0:
            messagebox.showerror("Error", "No negative values allowed!")
            return

        #add sa list ng appliances
        appliances.append({
            "name": name,
            "power": power,
            "hours": hours,
            "days": days
        })

        #clear inputs after mag-add para ready ulit mag-add ng next appliance if ever si user 
        entry_name.delete(0, tk.END)
        entry_power.delete(0, tk.END)
        entry_hours.delete(0, tk.END)
        entry_days.delete(0, tk.END)

        refresh_list()

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers only")

def refresh_list():
    #clear listbox
    listbox.delete(0, tk.END)

    #check kung empty, if ever walang laman show message langs
    if not appliances:
        listbox.insert(tk.END, "No appliances added.")
        return

    #display lahat ng appliances
    for i, app in enumerate(appliances, 1):
        kwh = (app["power"] * app["hours"] * app["days"]) / 1000
        listbox.insert(tk.END, f"{i}. {app['name']} - {kwh:.2f} kWh")

def calculate_bill():
    try:
        #kuha rate input per kWh
        rate = float(entry_rate2.get())

        if rate < 0:
            messagebox.showerror("Error", "Rate cannot be negative!")
            return

        # compute total kWh ng lahat ng appliances
        total_kwh = sum(
            (a["power"] * a["hours"] * a["days"]) / 1000
            for a in appliances
        )

        #final bill computation
        total_bill = total_kwh * rate

        result_label.config( #display result ng totaL result
            text=f"Total: {total_kwh:.2f} kWh | ₱{total_bill:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid rate")

def save_data():
    try:
        #save lahat ng appliances sa file
        save_to_file(appliances)
        messagebox.showinfo("Saved", "Data saved successfully!")
    except Exception:
        messagebox.showerror("Error", "Failed to save data")


def delete_selected():
    try: 
        # kuha yung selected item sa listbox tapos delete#delete selected item
        index = listbox.curselection()[0]
        appliances.pop(index)
        refresh_list()
    except IndexError:
        #kapag walang selected item
        messagebox.showerror("Error", "Select an item to delete")

def delete_all():
    #confirmation bago i-delete lahat
    confirm = messagebox.askyesno("Confirm", "Delete all appliances?")
    if confirm:
        appliances.clear()
        refresh_list()

#MAIN WINDOW
root = tk.Tk()
root.title("Electricity Bill Estimator")
root.geometry("700x800")
root.configure(bg="lightblue")

#UI ELEMENTS

#TITLE
title = ttk.Label(root, text="Electricity Bill Estimator",
                  font=("Helvetica", 16, "bold"))
title.pack(pady=10)

#RESULT DISPLAY
result_label = ttk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

#MANUAL CALCULATION SECTION
frame1 = ttk.LabelFrame(root, text="Manual Calculation", padding=10)
frame1.pack(fill="x", padx=40, pady=5)

entry_kwh = ttk.Entry(frame1)
entry_rate = ttk.Entry(frame1)

ttk.Label(frame1, text="kWh Used").grid(row=0, column=0)
entry_kwh.grid(row=0, column=1)

ttk.Label(frame1, text="Rate per kWh").grid(row=1, column=0)
entry_rate.grid(row=1, column=1)

ttk.Button(frame1, text="Calculate",
           command=manual_calculation).grid(row=2, columnspan=2, pady=5)

#ADD APPLIANCE SECTION
frame2 = ttk.LabelFrame(root, text="Add Appliance", padding=10)
frame2.pack(fill="x", padx=40, pady=5)

entry_name = ttk.Entry(frame2)
entry_power = ttk.Entry(frame2)
entry_hours = ttk.Entry(frame2)
entry_days = ttk.Entry(frame2)

ttk.Label(frame2, text="Name").grid(row=0, column=0)
entry_name.grid(row=0, column=1)

ttk.Label(frame2, text="Power (W)").grid(row=1, column=0)
entry_power.grid(row=1, column=1)

ttk.Label(frame2, text="Hours/day").grid(row=2, column=0)
entry_hours.grid(row=2, column=1)

ttk.Label(frame2, text="Days").grid(row=3, column=0)
entry_days.grid(row=3, column=1)

ttk.Button(frame2, text="Add Appliance",
           command=add_appliance).grid(row=4, columnspan=2, pady=5)

#LIST SECTION
frame3 = ttk.LabelFrame(root, text="Appliances List", padding=10)
frame3.pack(fill="both", expand=True, padx=40, pady=5)

listbox = tk.Listbox(frame3)
listbox.pack(fill="both", expand=True)

btn_frame = ttk.Frame(frame3)
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="Refresh",
           command=refresh_list).grid(row=0, column=0, padx=5)

ttk.Button(btn_frame, text="Delete Selected",
           command=delete_selected).grid(row=0, column=1, padx=5)

ttk.Button(btn_frame, text="Delete All",
           command=delete_all).grid(row=0, column=2, padx=5)

#TOTAL BILL SECTION
frame4 = ttk.LabelFrame(root, text="Total Bill Calculation", padding=10)
frame4.pack(fill="x", padx=40, pady=5)

entry_rate2 = ttk.Entry(frame4)

ttk.Label(frame4, text="Rate per kWh").grid(row=0, column=0)
entry_rate2.grid(row=0, column=1)

ttk.Button(frame4, text="Calculate Total",
           command=calculate_bill).grid(row=1, columnspan=2, pady=5)

#SAVE BUTTON
ttk.Button(root, text="Save Data", command=save_data).pack(pady=5)

#INITIAL LOAD
#load agad ng data pag open ng app
refresh_list()

root.mainloop()