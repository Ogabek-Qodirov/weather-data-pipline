import logging
import time

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from src.load import load_weather_data


# Logging configuration
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    start_time = time.time()

    # Cities and their coordinates
    cities = [
        {
            "name": "Tashkent",
            "latitude": 41.2995,
            "longitude": 69.2401
        },
        {
            "name": "Urgench",
            "latitude": 41.5500,
            "longitude": 60.6333
        },
        {
            "name": "Samarkand",
            "latitude": 39.6542,
            "longitude": 66.9597
        },
        {
            "name": "Bukhara",
            "latitude": 39.7681,
            "longitude": 64.4556
        }
    ]

    try:
        logging.info("Weather pipeline started!")

        for city in cities:

            print(f"\nProcessing {city['name']}...")

            # 1. EXTRACT
            hourly_data = extract_weather_data(
                city["latitude"],
                city["longitude"]
            )

            print("Extraction completed!")
            logging.info(f"Extracted data for {city['name']}")

            # 2. TRANSFORM
            df = transform_weather_data(
                hourly_data,
                city_name=city["name"]
            )

            print("Transformation completed!")

            # 3. VALIDATE
            validate_weather_data(df)

            print("Validation completed!")

            # 4. LOAD
            load_weather_data(df)

            print(f"{city['name']} completed!")

        duration = time.time() - start_time

        logging.info(
            f"Pipeline completed successfully in {duration:.2f} seconds"
        )

        print(f"\nAll cities processed in {duration:.2f} seconds!")

    except Exception:
        logging.exception("Weather pipeline failed!")
        print("Pipeline failed! Check pipeline.log for details.")
        raise


if __name__ == "__main__":
    main()
















