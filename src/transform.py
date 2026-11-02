
import pandas as pd


def transform_weather_data(hourly_data, city_name):
    """
    API dan kelgan hourly data ni
    Pandas DataFrame ga aylantiradi.
    """

    # Kerakli ma'lumotlarni ajratib olamiz
    weather_data = {
        "city": city_name,
        "time": hourly_data["time"],
        "temperature": hourly_data["temperature_2m"],
        "humidity": hourly_data["relative_humidity_2m"],
        "wind_speed": hourly_data["wind_speed_10m"]
    }

    # Dictionary ni DataFrame ga aylantiramiz
    df = pd.DataFrame(weather_data)

    # Vaqt ustunini datetime formatiga o'tkazamiz
    df["time"] = pd.to_datetime(df["time"])

    # DataFrame ni qaytaramiz
    return df
