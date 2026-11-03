
import pandas as pd


def transform_weather_data(hourly_data, city_name):
    """
    When data came from API that transforms the data into Pandas DataFrame .
    """

    # Extracting the data which we need
    weather_data = {
        "city": city_name,
        "time": hourly_data["time"],
        "temperature": hourly_data["temperature_2m"],
        "humidity": hourly_data["relative_humidity_2m"],
        "wind_speed": hourly_data["wind_speed_10m"]
    }

    #Transforming the Dictionary into Pandas Dataframe
    df = pd.DataFrame(weather_data)

    # Transfer to datatype into datetime
    df["time"] = pd.to_datetime(df["time"])

    # Returning the DataFrame
    return df
