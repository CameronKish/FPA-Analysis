import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('FPA.db')
cursor = conn.cursor()

# Retrieve the data from the ratio_table
cursor.execute("SELECT [Company], [Year], [Profit Margin], [Quick Ratio], [Debt to Equity Ratio], [Working Capital Ratio], [Return on Equity Ratio], [Return on Invested Capital (ROIC)] FROM ratio_table")
rows = cursor.fetchall()

# Create a dictionary to store the trends for each ratio
trends = {
    'Profit Margin': [],
    'Quick Ratio': [],
    'Debt to Equity Ratio': [],
    'Working Capital Ratio': [],
    'Return on Equity Ratio': [],
    'Return on Invested Capital (ROIC)': []
}

# Iterate over the rows and track trends for each ratio
previous_year_data = None
for row in rows:
    company = row[0]
    year = row[1]
    data = row[2:]

    # Check if it's the first year or a new company
    if previous_year_data is None or previous_year_data[0] != company:
        previous_year_data = data
        continue

    # Calculate the trends for each ratio
    for i in range(len(data)):
        ratio_name = list(trends.keys())[i]
        trend = 'Stable'

        if previous_year_data[i] < data[i]:
            trend = 'Increasing'
        elif previous_year_data[i] > data[i]:
            trend = 'Decreasing'

        trends[ratio_name].append((year, trend))

    previous_year_data = data

for ratio, trend_data in trends.items():
    print(f"Trends for {ratio}:")
    for data in trend_data:
        year, trend = data
        print(f"Year: {year}, Trend: {trend}")
    print()


'''
# Plot and display the trends for each ratio
for ratio, trend_data in trends.items():
    years = [data[0] for data in trend_data]
    trends = [data[1] for data in trend_data]

    plt.plot(years, trends, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Trend')
    plt.title(f"Trends for {ratio}")
    plt.grid(True)
    plt.show()
    # Print the x and y coordinates
    for year, trend in zip(years, trends):
        print(f"Coordinates: ({year}, {trend})")
    print()
'''