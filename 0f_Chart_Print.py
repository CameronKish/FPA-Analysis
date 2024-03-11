import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('FPA.db')
cursor = conn.cursor()

# Retrieve the data for profit margin over time
cursor.execute("SELECT [id], [Profit Margin] FROM ratio_table")
rows = cursor.fetchall()

# Separate the years and profit margins into separate lists
years = []
profit_margins = []
for row in rows:
    year = row[0]
    profit_margin = row[1]
    years.append(year)
    profit_margins.append(profit_margin)

# Plot the profit margin over time
plt.plot(years, profit_margins, marker='o')
plt.xlabel('Year')
plt.ylabel('Profit Margin')
plt.title('Profit Margin Over Time')
plt.grid(True)
plt.show()
