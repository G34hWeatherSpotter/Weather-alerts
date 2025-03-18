import fetch_alerts
import os

from fetch_alerts import fetch_weather_alerts, write_alerts_to_file

def main():
    # Path to the alerts file
    alerts_file_path = "alerts.txt"

    # Delete the old alerts file if it exists
    if os.path.exists(alerts_file_path):
        os.remove(alerts_file_path)
        print(f"Deleted old alerts file: {alerts_file_path}")

    # Fetch weather alerts from the API
    alerts = fetch_weather_alerts()

    # Save the new alerts to alerts.txt
    write_alerts_to_file(alerts)

    print("Weather alerts updated successfully.")

if __name__ == "__main__":
    main()
