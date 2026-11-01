import requests


def extract_weather_data(latitude, longitude):
    """
    Open-Meteo API orqali soatlik ob-havo ma'lumotlarini oladi.
    """

    # API manzili
    url = "https://api.open-meteo.com/v1/forecast"

    # API ga yuboriladigan parametrlar
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Tashkent",
        "forecast_days": 1
    }

    # API ga GET so'rov yuboramiz
    response = requests.get(url, params=params, timeout=30)

    # HTTP xatolarini tekshiramiz
    response.raise_for_status()

    # JSON javobni Python dictionary ga o'tkazamiz
    data = response.json()

    # Faqat soatlik ma'lumotlarni qaytaramiz
    return data["hourly"]
