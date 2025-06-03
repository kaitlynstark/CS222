import requests

LAT = 40.1934
LON = -85.3864

# Use f-string to insert LAT and LON
POINTS_URL = f"https://api.weather.gov/points/{LAT},{LON}"

def get_forecast_url():
    response = requests.get(POINTS_URL)
    response.raise_for_status()
    data = response.json()
    return data["properties"]["forecast"]

def get_forecast_data(forecast_url):
    response = requests.get(forecast_url)
    response.raise_for_status()
    data = response.json()
    return data["properties"]["periods"]

def display_forecast(periods):
    print("Forecast for Muncie, Indiana:\n")
    for period in periods:
        # Use f-strings to evaluate the values
        print(f"{period['name']}: {period['temperature']}°F")
        print(f"{period['detailedForecast']}\n")

def main():
    try:
        forecast_url = get_forecast_url()
        forecast_periods = get_forecast_data(forecast_url)
        display_forecast(forecast_periods)
    except requests.RequestException as e:
        print(f"HTTP Error: {e}")
    except KeyError as e:
        print(f"Data Error: Missing Key {e}")

if __name__ == "__main__":
    main()