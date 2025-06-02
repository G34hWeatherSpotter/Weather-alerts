import requests
import json

# The URL for the National Weather Service alerts
API_URL = "https://api.weather.gov/alerts/active"

# Open the alerts.txt file to append new alerts
with open("alerts.txt", "a") as file:
    try:
        # Send a GET request to the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Check for errors in the response

        # Parse the JSON response
        alerts = response.json().get("features", [])

        if not alerts:
            file.write("No active alerts at this time.\n")
        else:
            # Process each alert in the response
            for alert in alerts:
                alert_properties = alert.get("properties", {})
                alert_type = alert_properties.get("event", "Unknown Alert")
                issued = alert_properties.get("sent", "Unknown Time")
                expires = alert_properties.get("expires", "Unknown Time")
                area = ", ".join(alert_properties.get("areaDesc", ["Unknown Area"]))
                description = alert_properties.get("description", "No description available.")

                # Write alert details to the file
                file.write(f"ALERT TYPE: {alert_type}\n")
                file.write(f"Issued: {issued}\n")
                file.write(f"Expires: {expires}\n")
                file.write(f"Area: {area}\n")
                file.write(f"Description: {description}\n")
                file.write("#" * 30 + "\n")  # Separator for readability

    except requests.exceptions.RequestException as e:
        # If there was an error with the API request, log it
        file.write(f"Error fetching alerts: {e}\n")
