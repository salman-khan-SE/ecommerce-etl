# E-Commerce ETL Pipeline

## Project Overview

This project implements an end-to-end E-Commerce ETL pipeline for loading Superstore sales data into a MySQL database. It extracts raw CSV data, transforms the dataset for analysis, and loads the cleaned results into database tables.

## Technologies Used

- Python
- pandas
- SQLAlchemy
- MySQL / PyMySQL
- python-dotenv
- Apache Airflow
- VS Code

## ETL Workflow

1. **Extract**
   - Read raw CSV data from `data/Superstore.csv`
2. **Transform**
   - Clean duplicates
   - Normalize column names
   - Fill missing customer names
   - Calculate `profit_margin`
   - Aggregate sales by category
3. **Load**
   - Write cleaned data to MySQL tables: `superstore` and `sales_summary`

## Project Files

- `extract.py` — reads the raw dataset
- `transform.py` — performs cleaning and aggregation
- `load.py` — loads data into MySQL
- `main.py` — runs the full ETL pipeline
- `dags/dags.py` — defines Airflow DAG tasks for extract, transform, load
- `analysis.py` — example queries against the loaded MySQL data
- `data/Superstore.csv` — source dataset

## Setup Instructions

1. Create a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your database credentials:
   ```text
   DB_USER=root
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=ecommerce_etl
   ```

4. Run the pipeline locally:
   ```powershell
   python main.py
   ```

5. Run Airflow DAGs if Airflow is installed:
   - Initialize Airflow database and start scheduler/webserver
   - Use `dags/dags.py` to define the ETL workflow

## Future Improvements

- Add data validation and schema checks before loading
- Separate production and development configurations
- Add unit tests for each ETL step
- Use Docker for reproducible deployment
- Add data quality logging and monitoring
- Split Airflow DAGs into modular task definitions
