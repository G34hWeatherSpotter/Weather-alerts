import os
import time
import json
from fetch_alerts import fetch_weather_alerts, save_alerts_to_file

def load_existing_alerts(file_path='alerts.txt'):
    """Load existing alerts from the alerts.txt file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return None

def update_alerts():
    """Update alerts and compare to see if they changed."""
    new_alerts = fetch_weather_alerts()
    existing_alerts = load_existing_alerts()

    if new_alerts != existing_alerts:
        save_alerts_to_file(new_alerts)
        print("Alerts updated!")
    else:
        print("No new alerts.")

def main():
    """Main function to check for updates periodically."""
    while True:
        print("Checking for new weather alerts...")
        update_alerts()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
