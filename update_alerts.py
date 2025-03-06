import requests
import xml.etree.ElementTree as ET
from datetime import datetime

NWS_ALERTS_URL = "https://alerts.weather.gov/cap/us.php?x=1"

def fetch_alerts():
    try:
        response = requests.get(NWS_ALERTS_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error: Unable to fetch alerts. ({e})"

    try:
        root = ET.fromstring(response.content)
        alerts = root.findall(".//{http://www.w3.org/2005/Atom}entry")
    except ET.ParseError as e:
        return f"Error: Unable to parse alerts. ({e})"

    if not alerts:
        return "No active alerts."

    latest_alerts = []
    for alert in alerts[:5]:  # Get the latest 5 alerts
        title = alert.find("{http://www.w3.org/2005/Atom}title").text
        summary = alert.find("{http://www.w3.org/2005/Atom}summary").text
        updated = alert.find("{http://www.w3.org/2005/Atom}updated").text
        updated_time = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z")
        formatted_time = updated_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        latest_alerts.append(f"{title} ({formatted_time}): {summary}")

    return "\n".join(latest_alerts)

def update_alerts_file():
    alerts_text = fetch_alerts()
    with open("alerts.txt", "w") as file:
        file.write(alerts_text)

    print("Alerts updated successfully!")

if __name__ == "__main__":
    update_alerts_file()