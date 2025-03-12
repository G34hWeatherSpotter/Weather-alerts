
#Made With Help From ChatGPT
import requests
import xml.etree.ElementTree as ET
import time

NWS_ALERTS_URL = "https://api.weather.gov/alerts/active.atom?region_type=land"

def fetch_alerts():
    response = requests.get(NWS_ALERTS_URL)
    if response.status_code != 200:
        return "Error: Unable to fetch alerts."

    root = ET.fromstring(response.content)
    alerts = root.findall(".//{http://www.w3.org/2005/Atom}entry")

    if not alerts:
        return "No active alerts."

    latest_alerts = []
    for alert in alerts[:5]:  # Get the latest 5 alerts
        title = alert.find("{http://www.w3.org/2005/Atom}title").text
        summary = alert.find("{http://www.w3.org/2005/Atom}summary").text
        latest_alerts.append(f"{title}: {summary}")

    return "\n".join(latest_alerts)

def update_alerts_file():
    alerts_text = fetch_alerts()
    with open("alerts.txt", "w") as file:
        file.write(alerts_text)

if __name__ == "__main__":
    update_alerts_file()
