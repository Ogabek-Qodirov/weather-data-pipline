from unittest.mock import patch, Mock
from src.extract import extract_weather_data

@patch("src.extract.requests.get")  #insted of request.get() it creates fake function
def test_extract_weather_data(mock_get):

    # Create a fake API response
    mock_response = Mock()

    mock_response.json.return_value = {
        "hourly": {
            "time": ["2026-11-03T10:00"],
            "temperature_2m": [20.5],
            "relative_humidity_2m": [45],
            "wind_speed_10m": [10.2]
        }
    }

    # Configure the mock response
    mock_get.return_value = mock_response

    # Run extraction function
    result = extract_weather_data(41.2995, 69.2401)

    # Check the result
    assert "time" in result
    assert result["temperature_2m"] == [20.5]

    # Check that API was called
    mock_get.assert_called_once()

    # Check HTTP status
    mock_response.raise_for_status.assert_called_once()
