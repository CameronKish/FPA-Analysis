import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

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

# Define the function to fit the data
def polynomial_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the polynomial regression model
params, _ = curve_fit(polynomial_func, years, profit_margins)

# Generate predictions for the next five years
next_years = np.arange(max(years) + 1, max(years) + 6)
predictions = polynomial_func(next_years, *params)

# Plot the existing data and the predictions
plt.plot(years, profit_margins, marker='o', label='Existing Data')
plt.plot(next_years, predictions, marker='o', label='Predictions')
plt.xlabel('Year')
plt.ylabel('Profit Margin')
plt.title('Profit Margin Over Time')
plt.grid(True)
plt.legend()
plt.show()

# Print the predicted profit margins for the next five years
print('Predicted Profit Margins for the Next Five Years:')
for year, prediction in zip(next_years, predictions):
    print(f'Year: {year}, Profit Margin: {prediction}')
