import requests
from datetime import datetime

# Replace with actual API endpoint or method to fetch alerts
API_URL = "https://api.weather.gov/alerts/active"

# Function to fetch alerts from the weather API
def fetch_alerts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        alerts = response.json()['features']  # Assuming the alerts are under 'features' key
        
        with open('alerts.txt', 'a') as file:
            for alert in alerts:
                alert_type = alert['properties']['event']
                issued_time = alert['properties']['sent']
                expires_time = alert['properties']['expires']
                area = alert['properties']['areaDesc']
                description = alert['properties']['description']

                # Format and append each alert
                file.write(f"\n{alert_type}\n")
                file.write(f"Issued: {format_time(issued_time)}\n")
                file.write(f"Expires: {format_time(expires_time)}\n")
                file.write(f"Area: {area}\n")
                file.write(f"Description: {description}\n")
                file.write(f"# {'-'*30}\n")

# Function to format the time to a human-readable format
def format_time(time_str):
    time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
    return time_obj.strftime("%B %d, %Y, %I:%M %p UTC")

# Run the function to fetch and append alerts
fetch_alerts()
