import os
import pandas as pd
from sqlalchemy import create_engine

db_url = os.getenv("DATABASE_URL")
csv_path = os.getenv("CSV_PATH")

print(f"📥 Loading {csv_path} into {db_url}")

engine = create_engine(db_url)

df = pd.read_csv(csv_path, compression="gzip", nrows=1000)
print("✅ CSV loaded into pandas")

df.to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")
print("✅ Data written to Postgres successfully!")
