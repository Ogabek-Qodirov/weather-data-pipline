import requests

def extract_weather_data(latitude, longitude):
    #URL that information came from API
    url = "https://api.open-meteo.com/v1/forecast"

    #Params - this is argument that we need then we call the parametr and API send us what we need
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,"
                  "relative_humidity_2m,"
                  "wind_speed_10m",
        "timezone": "Asia/Tashkent",
        "forecast_days": 1
    }

    #We sent a get request to the server and then, we wait 30 seconds
    response = requests.get(url, params=params, timeout=30)

    response.raise_for_status()

    #Infromation came from API just show us json format we set the format what we need the iformation
    data = response.json()

    #That returns hourly section on the params convert into dict
    return data["hourly"]