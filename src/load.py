import os
"""" 1.import os does 2 thing actually that firs one it connect with .env file and 
    if we type Databae_url = something it brings with argument and it works with out current file
    2.import os does creating files and it brings path into one path """
from dotenv import load_dotenv #this load_dotenv function reads env file and bring to our file
from sqlalchemy import create_engine, text

load_dotenv()

def load_weather_data(df):
    #We get the url of the database with os and getenv functions
    database_url = os.getenv("DATABASE_URL")

    #This checks the url exists or not
    if not database_url:
        raise ValueError("DATABASE_URL not found!")

    #This creates connection with database
    engine = create_engine(database_url)

    #this one called (update+insert) we have a new row it inserts the data into the database and the table
    query = text("""
    INSERT INTO weather (city, time, temperature, humidity, wind_speed) 
    VALUES (:city, :time, :temperature, :humidity, :wind_speed) 
        ON CONFLICT (city, time) 
        DO UPDATE SET
            temperature = EXCLUDED.temperature,
            humidity = EXCLUDED.humidity,
            wind_speed = EXCLUDED.wind_speed
    """)
    #It opens the connection between with database and stats the transaction (If there is error it adds the data into database)
    #
    try:
        with engine.begin() as connection:

            for _, row in df.iterrows(): #it cycles the DataFrame row under row, it gives (row and index)

                connection.execute(query,{
                    "city": row["city"],
                    "time": row["time"].to_pydatetime(),
                    "temperature": float(row["temperature"]),
                    "humidity": float(row["humidity"]),
                    "wind_speed": float(row["wind_speed"]),

                }
            ) #connection.execute(query,{}) :city and :time parametr fills the database with data (list)
        print("Weather data successfully inserted!")

    finally:
        #Databse connection ending
        engine.dispose()
