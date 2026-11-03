# Weather Data Pipeline

An end-to-end ETL pipeline that collects weather data from the Open-Meteo API, transforms and validates it using Python and Pandas, and stores it in a Neon PostgreSQL database.

The pipeline processes weather data for four cities in Uzbekistan: Tashkent, Urgench, Samarkand, and Bukhara.

## Project Overview

This project demonstrates a practical batch data engineering workflow, from API data extraction to database storage and automated execution.

**Main objectives:**
- Extract weather data from an external API.
- Transform raw JSON data into structured tabular data.
- Validate data quality before loading.
- Store weather records in PostgreSQL.
- Prevent duplicate records using database UPSERT operations.
- Automate testing with GitHub Actions.
- Schedule daily pipeline execution using Windows Task Scheduler.

## Architecture

```text
       Open-Meteo API
              |
              v
       Extract (Python)
              |
              v
      Transform (Pandas)
              |
              v
       Data Validation
              |
              v
      Load (SQLAlchemy)
              |
              v
      Neon PostgreSQL
              |
              v
       SQL Analytics
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| Pandas | Data transformation |
| Requests | API integration |
| PostgreSQL | Data storage |
| Neon | Cloud PostgreSQL database |
| SQLAlchemy | Database connection and loading |
| Pytest | Unit testing |
| Git & GitHub | Version control |
| GitHub Actions | Continuous Integration |
| Windows Task Scheduler | Automated execution |

## Data Source

Weather data is collected from the [Open-Meteo API](https://open-meteo.com/).

The pipeline retrieves hourly:
- Temperature (°C)
- Relative humidity (%)
- Wind speed (km/h)
- Timestamp

## Project Structure

```text
02-weather-data-pipline/
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   └── load.py
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_validate.py
│   └── test_load.py
│
├── data/
│   └── .gitkeep
│
├── main.py
├── requirements.txt
├── run_pipline.bat
├── .gitignore
└── README.md
```

## Pipeline Workflow

### 1. Extraction

The pipeline sends HTTP requests to the Open-Meteo API and retrieves hourly weather data for each selected city.

### 2. Transformation

Pandas converts the API response into a structured DataFrame.

The transformation process includes:
- Renaming columns.
- Organizing weather measurements.
- Converting timestamps into datetime format.
- Adding the city name to each record.

### 3. Data Validation

Before loading, the pipeline checks:
- Empty datasets.
- Required columns.
- Missing values.
- Duplicate rows.
- Valid temperature ranges.
- Valid humidity values.
- Non-negative wind speed.

Invalid data raises an exception and prevents the loading step.

### 4. Loading

SQLAlchemy connects to the Neon PostgreSQL database and inserts the transformed records into the `weather` table.

The pipeline uses PostgreSQL `ON CONFLICT` to update existing records instead of inserting duplicates.

The unique key is based on:

```sql
UNIQUE (city, time)
```

### 5. SQL Analytics

Stored weather records can be queried using SQL for further analysis, such as:
- Average temperature by city.
- Maximum and minimum temperatures.
- Average humidity.
- Wind speed comparisons.

## Testing

Unit tests are implemented using Pytest.

The tests cover:
- API extraction.
- Data transformation.
- Data validation.
- Database loading logic.

Run tests locally:

```bash
python -m pytest -v
```

## Continuous Integration

GitHub Actions automatically runs the test suite when code is pushed to the `main` branch or when a pull request is created.

Workflow configuration:

```text
.github/workflows/test.yml
```

## Automated Scheduling

The pipeline is scheduled to run daily using **Windows Task Scheduler**.

A batch file (`run_pipline.bat`) executes the Python pipeline automatically.

Docker and WSL are not required.

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Ogabek-Qodirov/02-weather-data-pipline.git
cd 02-weather-data-pipline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=your_neon_postgresql_connection_string
```

Replace the placeholder with your own Neon PostgreSQL connection string.

**Important:** Never commit your `.env` file or database credentials to GitHub.

### 5. Run the pipeline

```bash
python main.py
```

## Future Improvements

- Add historical weather data collection.
- Implement retry logic for API failures.
- Introduce Airflow for advanced workflow orchestration.
- Add data visualization dashboards.
- Improve monitoring and alerting.
- Add integration tests with a test database.

## Author

**Og'abek Qodirov**

Information Systems and Technologies Student | Aspiring Data Engineer

- GitHub: [Ogabek-Qodirov](https://github.com/Ogabek-Qodirov)

---

*This project is part of my Data Engineering learning journey, focused on building practical ETL pipelines and reliable data systems.*