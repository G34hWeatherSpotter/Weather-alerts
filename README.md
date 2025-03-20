
(notice: all of the current changes that arent from github bot are final till offical start of severe weather season with a few bug fixes.)


# Weather Alerts

This repository contains the code for Weather Alerts, a project designed to provide timely and accurate weather notifications. The project is primarily written in Python with supplementary HTML for web components.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetches real-time weather data from various APIs.
- Sends weather alerts via email and/or SMS.
- Web interface to display current weather conditions and alerts.
- Configurable settings for different alert thresholds.

## Installation

To get started with Weather Alerts, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/G34hWeatherSpotter/Weather-alerts.git
    cd Weather-alerts
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up configuration:**
    - Copy the example configuration file and update it with your API keys and other settings.
    ```bash
    cp config.example.json config.json
    ```

## Usage

To run the Weather Alerts application, use the following command:

```bash
python main.py
