
# Weather Data Pipeline

An end-to-end data engineering project that extracts weather data from the Open-Meteo API, transforms and validates it using Python and Pandas, and loads it into a PostgreSQL database.

## Project Overview

This pipeline collects hourly weather data for four cities in Uzbekistan:

- Tashkent
- Urgench
- Samarkand
- Bukhara

## Architecture

Open-Meteo API
      |
      v
Python Extraction
      |
      v
Data Transformation (Pandas)
      |
      v
Data Validation
      |
      v
PostgreSQL (Neon)

## Technologies

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Neon Database
- python-dotenv
- Git and GitHub

## Features

- Extracts hourly weather data from Open-Meteo API
- Processes multiple cities
- Transforms API responses into structured DataFrames
- Validates data quality
- Loads data into PostgreSQL
- Uses UPSERT to prevent duplicate city/time records
- Implements logging and error handling
- Supports SQL analytics

## Project Structure

```text
src/
    extract.py
    transform.py
    validate.py
    load.py

main.py
requirements.txt
README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd 02-weather-data-pipline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=your_neon_database_url
```

Run the pipeline:

```bash
python main.py
```

## Database

The pipeline stores weather records in PostgreSQL.

Each record contains:

- city
- time
- temperature
- humidity
- wind_speed

A unique constraint on `(city, time)` supports UPSERT operations.

## Future Improvements

- Automated scheduling
- Docker containerization
- Unit testing with pytest
- Cloud deployment
- Data visualization dashboard
