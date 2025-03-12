import fetch_alerts
from fetch_alerts import fetch_weather_alerts, write_alerts_to_file

def main():
    # Fetch weather alerts from the API
    alerts = fetch_weather_alerts()

    # Save the alerts to alerts.txt
    write_alerts_to_file(alerts)

    print("Weather alerts updated successfully.")

if __name__ == "__main__":
    main()

