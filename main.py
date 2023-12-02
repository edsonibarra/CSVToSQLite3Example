import pandas as pd
import sqlite3


# Step 1: Read the CSV file into a Pandas DataFrame
csv_file_path = "netflix_titles.csv"
df = pd.read_csv(csv_file_path)

# Step 2: Connect to the SQLite database
db_path = "netflix_titles.sqlite"
conn = sqlite3.connect(db_path)

# Step 3: Write the DataFrame to the SQLite database
table_name = "movies"
df.to_sql(table_name, conn, index=False, if_exists="replace")

# Step 4: Close the connection
conn.close()
print("Data imported")