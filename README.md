# Electricity Bill Estimator (Python GUI)

## Project Description

The Electricity Bill Estimator is a Python-based graphical user interface (GUI) application that calculates electricity consumption and estimated billing. The system allows users to compute electricity costs using either manual input or appliance-based energy tracking with persistent storage[cite: 1, 4].

It simulates real-world electricity usage by allowing users to manage multiple appliances and compute total energy consumption in kilowatt-hours (kWh) through a user-friendly GUI[cite: 1].

---

## Features

### Manual Calculation
- Allows users to input total electricity consumption in kWh[cite: 1].
- Computes total bill using a given rate per kWh[cite: 1].

### Appliance Management System (CRUD)
- **Add Appliance:** Input details (name, power in watts, hours per day, days used)[cite: 1].
- **View Appliances:** Display all registered appliances along with their computed kWh consumption[cite: 1].
- **Update Appliance:** Modify existing appliance details[cite: 1].
- **Delete Appliance:** Remove appliance records from the system[cite: 1].

### Automatic Energy Computation & Persistence
- Calculates electricity usage automatically based on appliance data[cite: 1].
- **File Data Persistence:** Saves and loads appliance records from `appliances.txt` using `file_handler.py`[cite: 4].

### Graphical User Interface (GUI)
- Clean Tkinter interface (`gui.py`) for forms, interactive tables, and clear visual outputs[cite: 4].

---

## File Structure & Architecture

```text
electricity-bill-estimator-gui/
│
├── main.py                 # Entry point to launch the application
├── gui.py                  # Graphical User Interface layout and event handling
├── appliance_manager.py    # CRUD logic for managing appliance objects
├── calculation.py          # Math logic for kWh and bill computations
├── file_handler.py         # File I/O operations for saving/loading data
└── appliances.txt          # Plain text storage file for appliance records
```[cite: 4]

---

## Formula Used

### Appliance-Based Estimation
```text
kWh = (Power in Watts × Hours per Day × Days Used) / 1000
Bill = kWh × Rate per kWh
