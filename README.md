# 🚖 NYC Taxi Data Engineering Project

## 📌 Overview
This project builds an **end-to-end data pipeline** for NYC Yellow Taxi data using **Docker, PostgreSQL, and Python**.  
The pipeline ingests raw CSV/Parquet data into a PostgreSQL database, making it easy to run queries and perform analysis.  

This project demonstrates core **Data Engineering skills**:
- Working with Dockerized services
- Data ingestion with Python & Pandas
- Database design and SQL queries
- Managing environments with Docker Compose
- Using pgAdmin for database exploration

---

## 🛠 Tech Stack
- **Python** (Pandas, SQLAlchemy)
- **PostgreSQL**
- **Docker & Docker Compose**
- **pgAdmin**

---

## ⚙️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/GhadaFaress/nyc-taxi-data-engineering.git
cd nyc-taxi-data-engineering

2. Start Services with Docker

Start all services using Docker Compose:

docker-compose up


This will launch:

PostgreSQL database

pgAdmin web UI

3. Access Services

Open pgAdmin: http://localhost:8080

Connect to the database: postgres:5432

4. Load Data into Database

Run the Python ingestion script to load the taxi trip data into PostgreSQL:

python ingest_data.py \
  --user=postgres \
  --password=postgres \
  --host=localhost \
  --port=5432 \
  --db=taxi \
  --table_name=yellow_taxi_data \
  --url=<data-url>

5. Run Analytics

After loading the data, run the analysis script:

python yellow_taxi_analysis.py

Example Query

Example SQL query to calculate the average fare per passenger count:

SELECT passenger_count, AVG(total_amount) AS avg_amount
FROM yellow_taxi_data
GROUP BY passenger_count
ORDER BY avg_amount DESC;

Project Highlights

Containerized environment for reproducibility

Automated data ingestion pipeline

SQL-based analytics on taxi trips

Clear modular structure (ingestion + analysis)

Future Improvements

Add Airflow for workflow orchestration

Automate dataset downloads

Deploy database on the cloud

Build dashboards (e.g., with PowerBI or Tableau
### 2\. Start Services with Docker * Start all services using Docker Compose: bash Copy code `docker-compose up` * This will launch: * PostgreSQL database * pgAdmin web UI ### 3\. Access Services * Open pgAdmin: [http://localhost:8080](http://localhost:8080) * Connect to the database: `
