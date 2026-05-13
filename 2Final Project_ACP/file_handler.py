#file_handler.py
def save_to_file(appliances):
    try:
        with open("appliances.txt", "w") as file:
            for app in appliances:
                line = f"{app['name']},{app['power']},{app['hours']},{app['days']}\n"
                file.write(line)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file():
    appliances = []

    try:
        with open("appliances.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 4:
                    continue

                name, power, hours, days = parts

                appliances.append({
                    "name": name,
                    "power": float(power),
                    "hours": float(hours),
                    "days": float(days)
                })

    except FileNotFoundError:
        pass

    return appliances