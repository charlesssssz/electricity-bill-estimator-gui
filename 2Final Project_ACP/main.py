#main.py
from file_handler import load_from_file, save_to_file
from appliance_manager import (
    add_appliance,
    view_appliances,
    delete_appliance,
    delete_all
)
from calculation import manual_calculation, calculate_bill

def main():
    appliances = load_from_file()
   
    choice = input("Start system? (y/n): ").lower()

    if choice != "y":
        print("Exited.")
        return

    while True:
        print("\nELECTRICITY BILL ESTIMATOR")
        print("1. Manual Calculation")
        print("2. Add Appliance")
        print("3. View Appliances")
        print("4. Delete Appliance")
        print("5. Delete All")
        print("6. Calculate Bill")
        print("7. Save & Exit")

        choice = input("Choose: ")

        if choice == "1":
            manual_calculation()

        elif choice == "2":
            add_appliance(appliances)

        elif choice == "3":
            view_appliances(appliances)

        elif choice == "4":
            delete_appliance(appliances)

        elif choice == "5":
            delete_all(appliances)

        elif choice == "6":
            calculate_bill(appliances)

        elif choice == "7":
            save_to_file(appliances)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()