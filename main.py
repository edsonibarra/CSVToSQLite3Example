import pandas as pd
import sqlite3


csv_file_path = "netflix_titles.csv"
df = pd.read_csv(csv_file_path)

db_path = "netflix_titles.sqlite"
conn = sqlite3.connect(db_path)

table_name = "movies"
df.to_sql(table_name, conn, index=False, if_exists="replace")

conn.close()
print("Data imported")