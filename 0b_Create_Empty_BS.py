import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('FPA.db')

# Create the table with the specified columns
create_table_query = '''
CREATE TABLE IF NOT EXISTS balance_sheet (
    Account TEXT,
    "12/31/2022" REAL,
    "12/31/2021" REAL
);
'''

# Execute the create table query
conn.execute(create_table_query)

# Close the database connection
conn.close()

print("Table created successfully!")


import pandas as pd


# Path to the Excel file
excel_file = "Financial_Report.xlsx"

# Connect to the SQLite database
conn = sqlite3.connect("FPA.db")
cursor = conn.cursor()

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name="Consolidated Balance Sheets")

# Drop any existing data in the income_statement table
cursor.execute("DELETE FROM balance_sheet")

# Iterate over each row in the DataFrame and insert into the income_statement table
for row in df.itertuples(index=False):
    account = row[0]
    value_2022 = row[1]
    value_2021 = row[2]
    
    cursor.execute("INSERT INTO balance_sheet (Account, `12/31/2022`, `12/31/2021`) VALUES (?, ?, ?)",
                   (account, value_2022, value_2021))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into the balance_sheet table.")
