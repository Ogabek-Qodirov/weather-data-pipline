
def validate_weather_data(df):
    """
    Weather DataFrame ma'lumotlarini tekshiradi.
    """

    # 1. DataFrame bo'sh emasligini tekshiramiz
    if df.empty:
        raise ValueError("DataFrame is empty!")

    # 2. Kerakli ustunlar mavjudligini tekshiramiz
    required_columns = [
        "time",
        "temperature",
        "humidity",
        "wind_speed"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # 3. Bo'sh qiymatlarni tekshiramiz
    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found!")

    # 4. Takroriy qatorlarni tekshiramiz
    if df.duplicated().any():
        raise ValueError("Duplicate rows found!")

    # 5. Haroratni tekshiramiz
    if not df["temperature"].between(-90, 60).all():
        raise ValueError("Invalid temperature!")

    # 6. Namlikni tekshiramiz
    if not df["humidity"].between(0, 100).all():
        raise ValueError("Invalid humidity!")

    # 7. Shamol tezligini tekshiramiz
    if (df["wind_speed"] < 0).any():
        raise ValueError("Invalid wind speed!")

    print("All data validation checks passed!")

    return True
