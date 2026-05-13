#calculation.py
def manual_calculation():
    print("\nManual Calculation")

    try:
        kwh = float(input("Enter total kWh used: "))
        rate = float(input("Enter rate per kWh: "))

        if kwh < 0 or rate < 0:
            print("Invalid input!")
            return

        total = kwh * rate
        print(f"Total Bill: ₱{total:.2f}")

    except ValueError:
        print("Error: Numbers only!")


def calculate_bill(appliances):
    print("\n--- Appliance-Based Calculation ---")

    if not appliances:
        print("No appliances found.")
        return

    try:
        rate = float(input("Enter rate per kWh: "))

        if rate < 0:
            print("Invalid rate!")
            return

        total_kwh = sum(
            (a["power"] * a["hours"] * a["days"]) / 1000
            for a in appliances
        )

        print(f"\nTotal kWh: {total_kwh:.2f}")
        print(f"Estimated Bill: ₱{total_kwh * rate:.2f}")

    except ValueError:
        print("Invalid input!")