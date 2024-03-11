import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("FPA.db")
cursor = conn.cursor()

# Create the ratio_table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratio_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Company TEXT,
        Year REAL,
        "Profit Margin" REAL,
        "Quick Ratio" REAL,
        "Debt to Equity Ratio" REAL,
        "Working Capital Ratio" REAL,
        "Return on Equity Ratio" REAL,
        "Return on Invested Capital (ROIC)" REAL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("ratio_table created successfully.")
