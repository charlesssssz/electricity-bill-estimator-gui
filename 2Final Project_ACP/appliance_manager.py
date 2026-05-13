#appliance_manager.py
def add_appliance(appliances):
    print("\nAdd Appliance")

    while True:
        try:
            name = input("Appliance name: ").strip()
            power = float(input("Power (Watts): "))
            hours = float(input("Hours per day: "))
            days = float(input("Days used: "))

            if name == "" or power < 0 or hours < 0 or days < 0:
                print("Invalid input. Try again.\n")
                continue

            appliances.append({
                "name": name,
                "power": power,
                "hours": hours,
                "days": days
            })

            print("Appliance added successfully!")

        except ValueError:
            print("Error: Numbers only!")
            continue

        if input("Add another? (y/n): ").lower() != "y":
            break


def view_appliances(appliances):
    print("\nAppliance List")

    if not appliances:
        print("No appliances added.")
        return

    for i, app in enumerate(appliances, 1):
        kwh = (app["power"] * app["hours"] * app["days"]) / 1000
        print(f"{i}. {app['name']} | {kwh:.2f} kWh")


def delete_appliance(appliances):
    print("\nDelete Appliance")

    if not appliances:
        print("No appliances to delete.")
        return

    for i, app in enumerate(appliances, 1):
        print(f"{i}. {app['name']}")

    try:
        choice = int(input("Enter number to delete: ")) - 1

        if choice < 0 or choice >= len(appliances):
            print("Invalid selection.")
            return

        removed = appliances.pop(choice)
        print(f"{removed['name']} deleted.")

    except ValueError:
        print("Invalid input!")


def delete_all(appliances):
    print("\nDelete All Appliances")

    if not appliances:
        print("No appliances to delete.")
        return

    if input("Are you sure? (y/n): ").lower() == "y":
        appliances.clear()
        print("All appliances deleted.")
    else:
        print("Cancelled.")