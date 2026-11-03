import pandas as pd
from src.transform import transform_weather_data

def test_transform_weather_data():

    #Sample input data
    hourly_data = {
        "time": ["2026-11-03T10:00", "2026-11-03T11:00"],
        "temperature_2m": [20.5, 22.0],
        "relative_humidity_2m": [45, 50],
        "wind_speed_10m": [10.2, 12.5]
    }

    #Run transformation
    df = transform_weather_data(hourly_data, "Tashkent")

    #Checking output
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == [
        "city", "time", "temperature", "humidity", "wind_speed"
    ]
    assert df["city"].iloc[0] == "Tashkent"
    assert df["temperature"].iloc[0] == 20.5
