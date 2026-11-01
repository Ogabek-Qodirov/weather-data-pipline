
from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data

def main():

    # Toshkent koordinatalari
    latitude = 41.2995
    longitude = 69.2401

    # API dan ob-havo ma'lumotlarini olamiz
    hourly_data = extract_weather_data(latitude, longitude)

    # Olingan ma'lumotlarni tekshiramiz
    print(hourly_data.keys())

    # Birinchi 5 ta haroratni chiqaramiz
    print(hourly_data["temperature_2m"][:5])


if __name__ == "__main__":
    main()

def main():

    # Toshkent koordinatalari
    latitude = 41.2995
    longitude = 69.2401

    # 1. EXTRACT
    hourly_data = extract_weather_data(latitude, longitude)

    print("Weather data extracted successfully!")

    # 2. TRANSFORM
    df = transform_weather_data(hourly_data)

    print("Weather data transformed successfully!")

    # Natijani ko'ramiz
    print(df.head())

    # DataFrame haqida ma'lumot
    print(df.info())


if __name__ == "__main__":
    main()


def main():

    latitude = 41.2995
    longitude = 69.2401

    # 1. EXTRACT
    hourly_data = extract_weather_data(latitude, longitude)
    print("1. Extraction completed!")

    # 2. TRANSFORM
    df = transform_weather_data(hourly_data)
    print("2. Transformation completed!")

    # 3. VALIDATE
    validate_weather_data(df)
    print("3. Validation completed!")

    # Natijani ko'rsatamiz
    print(df.head())


if __name__ == "__main__":
    main()