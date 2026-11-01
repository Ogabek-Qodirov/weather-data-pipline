# Weather Data Pipeline

An end-to-end Data Engineering project that collects hourly weather data from the Open-Meteo API, transforms and validates it using Python and Pandas, and stores it in a cloud PostgreSQL database.

## Project Overview

The pipeline follows the ETL architecture:

1. **Extract** — Collect hourly weather data from Open-Meteo API.
2. **Transform** — Convert JSON responses into Pandas DataFrames and clean the data.
3. **Validate** — Check missing values, duplicates, and invalid measurements.
4. **Load** — Store processed weather data in PostgreSQL.

## Technologies

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Google Colab
- Neon

## Project Status

Currently developing the API extraction and data transformation stages.

## Data Source

[Open-Meteo API](https://open-meteo.com/)

## Project Goals

- Build an end-to-end ETL pipeline.
- Practice API integration and data processing.
- Work with cloud PostgreSQL databases.
- Develop practical Data Engineering skills.