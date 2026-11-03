import pandas as pd
from unittest.mock import patch, MagicMock

from src.load import load_weather_data


@patch("src.load.create_engine")
@patch("src.load.os.getenv")
def test_load_weather_data(mock_getenv, mock_create_engine):

    # Fake database URL
    mock_getenv.return_value = "postgresql://fake-url"

    # Create fake database engine
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    # Create sample weather data
    df = pd.DataFrame({
        "city": ["Tashkent"],
        "time": [pd.Timestamp("2026-11-03 10:00")],
        "temperature": [20.5],
        "humidity": [45],
        "wind_speed": [10.2]
    })

    # Run loading function
    load_weather_data(df)

    # Check database connection
    mock_create_engine.assert_called_once()

    # Check that SQL execution happened
    mock_connection = mock_engine.begin.return_value.__enter__.return_value
    mock_connection.execute.assert_called_once()

    # Check that database engine was closed
    mock_engine.dispose.assert_called_once()