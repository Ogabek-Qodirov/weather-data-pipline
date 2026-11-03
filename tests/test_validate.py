import pandas as pd
import pytest

from src.validate import validate_weather_data


def test_valid_weather_data():
    # Create valid sample data
    df = pd.DataFrame({
        "time": ["2026-11-03 10:00"],
        "temperature": [20.5],
        "humidity": [45],
        "wind_speed": [10.2]
    })

    # Validation should return True
    assert validate_weather_data(df) is True


def test_empty_dataframe():
    # Empty data should raise ValueError
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty"):
        validate_weather_data(df)


def test_missing_values():
    # Create data with a missing temperature
    df = pd.DataFrame({
        "time": ["2026-11-03 10:00"],
        "temperature": [None],
        "humidity": [45],
        "wind_speed": [10.2]
    })

    with pytest.raises(ValueError, match="Missing values found"):
        validate_weather_data(df)


def test_invalid_temperature():
    # Temperature cannot exceed 60
    df = pd.DataFrame({
        "time": ["2026-11-03 10:00"],
        "temperature": [100],
        "humidity": [45],
        "wind_speed": [10.2]
    })

    with pytest.raises(ValueError, match="Invalid temperature"):
        validate_weather_data(df)