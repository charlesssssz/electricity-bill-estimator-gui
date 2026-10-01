# Electricity Bill Estimator (Python GUI)

## Project Description

The **Electricity Bill Estimator** is a Python-based graphical user interface (GUI) application designed to compute electricity consumption and estimate billing costs. It allows users to calculate costs via manual input or track energy usage per appliance with persistent storage[cite: 1, 4].

The system provides an intuitive interface for managing appliances, calculating total energy consumption in kilowatt-hours (kWh), and viewing overall costs[cite: 1].

---

## Key Features

* **Manual Calculation:** Instantly calculates the total bill using manual kWh consumption input and a custom rate per kWh[cite: 1].
* **Appliance Management (CRUD):**
  * **Add:** Register new appliances with power rating (Watts), daily usage hours, and days used[cite: 1].
  * **View:** Display all saved appliances and their computed kWh consumption[cite: 1].
  * **Update:** Edit existing appliance details[cite: 1].
  * **Delete:** Remove unwanted appliance records[cite: 1].
* **Data Persistence:** Automatically saves and loads appliance data using `appliances.txt` so records persist across sessions[cite: 4].
* **Graphical User Interface:** User-friendly GUI layout with input forms, interactive tables, and action buttons[cite: 1, 4].

---

## File Architecture

```text
electricity-bill-estimator-gui/
├── main.py                 # Application entry point
├── gui.py                  # Tkinter GUI layout and user interactions
├── appliance_manager.py    # Core CRUD logic for managing appliances
├── calculation.py          # Math formulas for kWh and bill computations
├── file_handler.py         # File I/O operations (reads/writes appliances.txt)
├── appliances.txt          # Data storage file
└── practice concept.py     # Sandbox / testing script
```[cite: 4]

---

## Formulas Used

### Appliance-Based Estimation
```text
kWh = (Power in Watts × Hours per Day × Days Used) / 1000
Bill = kWh × Rate per kWh
