import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# ✅ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    revenue REAL,
    cost REAL,
    date TEXT
)
""")

# ✅ Insert dummy data
start_date = datetime(2022, 1, 1)

for i in range(2000):
    date = start_date + timedelta(days=random.randint(0, 1000))
    revenue = round(random.uniform(100, 10000), 2)
    cost = round(revenue * random.uniform(0.5, 0.9), 2)

    cursor.execute("""
    INSERT INTO sales (customer_id, revenue, cost, date)
    VALUES (?, ?, ?, ?)
    """, (random.randint(1, 500), revenue, cost, date.strftime('%Y-%m-%d')))

conn.commit()
conn.close()

print("✅ Database with sample data created!")