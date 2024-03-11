import sqlite3

# Connect to the database
conn = sqlite3.connect('FPA.db')
cursor = conn.cursor()

# Retrieve the values for Gross Profit, Sales, net, Total Current Assets, Inventories, Total Current Liabilities, Total Liabilities, Total Stockholders' Equity, Net Income, Dividend Payments, and Invested Capital
cursor.execute("SELECT [12/31/2022] FROM income_statement WHERE Account = 'Gross profit'")
gross_profit = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM income_statement WHERE Account = 'Sales, net'")
sales_net = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Total current assets'")
total_current_assets = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Inventories'")
inventories = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Total current liabilities'")
total_current_liabilities = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Total liabilities'")
total_liabilities = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Total stockholders'' equity'")
total_stockholders_equity = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM income_statement WHERE Account = 'Net income'")
net_income = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Long-term debt, net'")
longterm_debt = float(cursor.fetchone()[0])

cursor.execute("SELECT [12/31/2022] FROM balance_sheet WHERE Account = 'Current portion of long-term debt'")
longterm_debtcurrent = float(cursor.fetchone()[0])

# Calculate the ratios
profit_margin = gross_profit / sales_net
quick_ratio = (total_current_assets - inventories) / total_current_liabilities
debt_to_equity_ratio = total_liabilities / total_stockholders_equity
working_capital_ratio = total_current_assets / total_current_liabilities
return_on_equity_ratio = net_income / total_stockholders_equity
invested_capital = total_stockholders_equity + longterm_debt + longterm_debtcurrent
roic = net_income / invested_capital

#Other
company = "Advanced Energy Industries, Inc."
year_end = "12/31/2022"

# Insert the ratios into the ratio_table
#cursor.execute("INSERT INTO ratio_table ('Company', 'Year', 'Profit Margin', 'Quick Ratio', 'Debt to Equity Ratio', 'Working Capital Ratio', 'Return on Equity Ratio', 'Return on Invested Capital (ROIC)') VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
#               (company, year_end, profit_margin, quick_ratio, debt_to_equity_ratio, working_capital_ratio, return_on_equity_ratio, roic))

# Get the column names of the income_statement table
cursor.execute("SELECT * FROM income_statement LIMIT 1")
columns = [description[0] for description in cursor.description[1:]]

for column in columns:
    print(column)


# Commit the changes
conn.commit()

# Close the connection
conn.close()
