import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="taxi",
    user="user",
    password="postgres",
)

df=pd.read_sql_query("SELECT * FROM yellow_taxi_data LIMIT 1000;", conn)

print(df.head())
print(df.describe())

print("Average fare:", df["fare_amount"].mean())

total_trips = len(df)
print("Total trips:", total_trips)

avg_fare = df['total_amount'].mean()
print("Average fare:", avg_fare)


max_fare = df['total_amount'].max()
min_fare = df['total_amount'].min()
print("Max fare:", max_fare, "Min fare:", min_fare)


trips_per_passenger = df.groupby('passenger_count').size()
print(trips_per_passenger)


avg_distance = df['trip_distance'].mean()
print("Average trip distance:", avg_distance)


fare_by_vendor = df.groupby('VendorID')['total_amount'].sum()
print(fare_by_vendor)


neg_fares = df[df['total_amount'] < 0]
neg_distance = df[df['trip_distance'] < 0]
print("Negative fares:\n", neg_fares)
print("Negative distances:\n", neg_distance)


top_fares = df.nlargest(5, 'total_amount')
print(top_fares)


congestion_trips = df[df['congestion_surcharge'] > 0].shape[0]
print("Trips with congestion surcharge:", congestion_trips)


avg_fare_passenger = df.groupby('passenger_count')['total_amount'].mean()
print(avg_fare_passenger)
