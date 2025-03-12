import requests
from datetime import datetime

# The URL to get all active alerts across the United States
API_URL = "https://api.weather.gov/alerts/active"

# Function to fetch alerts from the weather.gov API
def fetch_alerts():
    # Make a request to fetch the active alerts from the National Weather Service
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        # Parse the JSON response
        alerts = response.json()['features']
        
        # Open the alerts.txt file to append new alerts
        with open('alerts.txt', 'a') as file:
            for alert in alerts:
                # Extract the alert information
                alert_type = alert['properties']['event']
                issued_time = alert['properties']['sent']
                expires_time = alert['properties']['expires']
                area = alert['properties']['areaDesc']
                description = alert['properties']['description']
                
                # Write each alert to the file
                file.write(f"\n{alert_type}\n")
                file.write(f"Issued: {format_time(issued_time)}\n")
                file.write(f"Expires: {format_time(expires_time)}\n")
                file.write(f"Area: {area}\n")
                file.write(f"Description: {description}\n")
                file.write(f"# {'-'*30}\n")
    
    else:
        print(f"Failed to fetch alerts, Status Code: {response.status_code}")

# Function to format the time to a human-readable format
def format_time(time_str):
    # Parse the time from the API response into a datetime object
    time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
    # Return the formatted time string
    return time_obj.strftime("%B %d, %Y, %I:%M %p UTC")

# Run the function to fetch and append alerts to alerts.txt
fetch_alerts()
