
def validate_weather_data(df):
    """
    Weather DataFrame validation.
    """

    # 1. Making sure of the dataframe is not empty
    if df.empty:
        raise ValueError("DataFrame is empty!")

    # 2. Validating the required columns exists
    required_columns = [
        "time",
        "temperature",
        "humidity",
        "wind_speed"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # 3. Checking there is not missing value
    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found!")

    # 4. Validating there is no duplicate rows
    if df.duplicated().any():
        raise ValueError("Duplicate rows found!")

    # 5. Validating the temperature
    if not df["temperature"].between(-90, 60).all():
        raise ValueError("Invalid temperature!")

    if not df["humidity"].between(0, 100).all():
        raise ValueError("Invalid humidity!")

    if (df["wind_speed"] < 0).any():
        raise ValueError("Invalid wind speed!")

    print("All data validation checks passed!")

    return True
