import requests
import json
import os

# URL for the weather alert API
API_URL = "https://api.weather.gov/alerts/active"

# File where the alerts will be stored
ALERTS_FILE = "alerts.txt"

# Function to fetch alerts from the API
def fetch_weather_alerts():
    try:
        # Make the GET request to the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parse the response JSON
        alerts_data = response.json()

        # Check if there are any active alerts
        if alerts_data.get('features'):
            return alerts_data['features']
        else:
            print("No active alerts at the moment.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather alerts: {e}")
        return None

# Function to write the fetched alerts to a file
def write_alerts_to_file(alerts):
    try:
        with open(ALERTS_FILE, "w") as file:
            json.dump(alerts, file, indent=4)  # Writing alerts as a JSON for structured data
        print(f"Weather alerts have been saved to {ALERTS_FILE}")
    except Exception as e:
        print(f"Error writing to {ALERTS_FILE}: {e}")

# Main execution
def main():
    print("Fetching weather alerts...")
    alerts = fetch_weather_alerts()

    if alerts:
        write_alerts_to_file(alerts)
    else:
        print("No new alerts to save.")

if __name__ == "__main__":
    main()
