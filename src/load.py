import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

def load_weather_data(df):
    #Database URL ni olamiz
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL not found!")

    engine = create_engine(database_url)

    #Upsert uchun SQL query
    query = text("""INSERT INTO weather (city, time, temperature, humidity, wind_speed) 
    VALUES (:city, :time, :temperature, :humidity, :wind_speed) 
        ON CONFLICT (city, time) 
        DO UPDATE SET
            temperature = EXCLUDED.temperature,
            humidity = EXCLUDED.humidity,
            wind_speed = EXCLUDED.wind_speed
    """)

    try:
        with engine.begin() as connection:

            for _, row in df.iterrows():

                connection.execute(query,{
                    "city": row["city"],
                    "time": row["time"].to_pydatetime(),
                    "temperature": float(row["temperature"]),
                    "humidity": float(row["humidity"]),
                    "wind_speed": float(row["wind_speed"]),

                }
            )

        print("Weather data successfully inserted!")

    finally:
        #Databse connectioni yopish
        engine.dispose()
